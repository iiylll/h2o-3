package water.rapids;

import water.*;
import water.fvec.Chunk;

class RadixCount extends MRTask<RadixCount> {
  static class Long2DArray extends Iced {
    Long2DArray(int len) { _val = new long[len][]; }
    long _val[][];
  }
  private Long2DArray _counts;
  private final int _shift;
  private final int _col;
  private final long _base;
  private final double _baseD;
  // used to determine the unique DKV names since DF._key is null now and
  // before only an RTMP name anyway
  private final boolean _isLeft; 
  private final int _id_maps[][];
  private final boolean _isNotDouble;

  RadixCount(boolean isLeft, long base, int shift, int col, int id_maps[][], boolean isNotDouble, double baseD) {
    _isLeft = isLeft;
    _base = base;
    _col = col;
    _shift = shift;
    _id_maps = id_maps;
    _isNotDouble = isNotDouble;
    _baseD = baseD;
  }

  // make a unique deterministic key as a function of frame, column and node
  // make it homed to the owning node
  static Key getKey(boolean isLeft, int col, H2ONode node) {
    return Key.make("__radix_order__MSBNodeCounts_col" + col + "_node" + node.index() + (isLeft ? "_LEFT" : "_RIGHT"));
    // Each node's contents is different so the node number needs to be in the key
    // TODO: need the biggestBit in here too, that the MSB is offset from
  }

  @Override protected void setupLocal() {
    _counts = new Long2DArray(_fr.anyVec().nChunks());
  }

  @Override public void map( Chunk chk ) {
    long tmp[] = _counts._val[chk.cidx()] = new long[256];
    // TODO: assert chk instanceof integer or enum; -- but how since many
    // integers (C1,C2 etc)?  Alternatively: chk.getClass().equals(C8Chunk.class)
    if (!(_isLeft && chk.vec().isCategorical())) {
      if (chk.vec().naCnt() == 0) {
        // There are no NA in this join column; hence branch-free loop. Most
        // common case as should never really have NA in join columns.
        for (int r=0; r<chk._len; r++) {
          if (_isNotDouble) {
            tmp[(int) ((chk.at8(r) - _base + 1) >> _shift)]++;
          } else {
            long ctrVal = Double.doubleToRawLongBits(chk.atd(r)-_baseD+1)>>_shift;
            tmp[(int) ctrVal]++;
          }
        }
      } else {
        // There are some NA in the column so have to branch.  TODO: warn user
        // NA are present in join column
        for (int r=0; r<chk._len; r++) {
          if (chk.isNA(r)) tmp[0]++;
          else {
            if (_isNotDouble) {
              tmp[(int) ((chk.at8(r) - _base + 1) >> _shift)]++;
            } else {
              long ctrVal = Double.doubleToRawLongBits(chk.atd(r)-_baseD+1)>>_shift;
              tmp[(int) ctrVal]++;
            }
          }

          // Done - we will join NA to NA as data.table does
          // TODO: allow NA-to-NA join to be turned off.  Do that in bmerge as a simple low-cost switch.
          // Note that NA and the minimum may well both be in MSB 0 but most of
          // the time we will not have NA in join columns
        }
      }
    } else {
      // first column (for MSB split) in an Enum
      // map left categorical to right levels using _id_maps
      assert _id_maps[0].length > 0;
      assert _base==0;
      if (chk.vec().naCnt() == 0) {
        for (int r=0; r<chk._len; r++) {
          tmp[(_id_maps[0][(int)chk.at8(r)]+1) >> _shift]++;
        }
      } else {
        for (int r=0; r<chk._len; r++) {
          if (chk.isNA(r)) tmp[0]++;
          else tmp[(_id_maps[0][(int)chk.at8(r)]+1) >> _shift]++;
        }
      }
    }
  }

  @Override protected void closeLocal() {
    DKV.put(getKey(_isLeft, _col, H2O.SELF), _counts, _fs, true);
    // just the MSB counts per chunk on this node.  Most of this spine will be empty here.  
    // TODO: could condense to just the chunks on this node but for now, leave sparse.
    // We'll use this sparse spine right now on this node and the reduce happens on _o and _x later
  }
}
