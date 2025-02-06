import numpy as np


def IQR_filter(arr):
  '''
  param: 1d or 2d np.array(), the swot height.
  retrun: numpy MaskedArray, the filtered swot height.
  '''
  Q1, Q3 = np.nanpercentile(arr, (25, 75))
  IQR = Q3 - Q1
  wse_low_thre, wse_high_thre = Q1 - 1.5*IQR, Q3 + 1.5*IQR 
  arr_masked = np.ma.masked_where(np.logical_or(arr>wse_high_thre, arr<wse_low_thre), arr)
  return arr_masked, IQR


def toslant(pixc, key='height'):
    az = pixc.azimuth_index.astype(int)
    rng = pixc.range_index.astype(int)
    out_arr = np.zeros((pixc.interferogram_size_azimuth + 1, \
                    pixc.interferogram_size_range + 1)) + np.nan
    # handle complex interferogram
    if key=='interferogram':
        out_arr = out_arr.astype('complex64')
        var = pixc[key][:,0] + 1j * pixc[key][:,1]
    else:
        var = pixc[key]
    out_arr[az, rng] = var
    return out_arr

