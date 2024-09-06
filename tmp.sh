path_nc=data/dianchi_test/SWOT_L2_HR_Raster_100m_UTM48R_N_x_x_x_015_049_099F_20240510T014706_20240510T014727_PIC0_01.nc
path_tif=data/dianchi_test/SWOT_L2_HR_Raster_100m_UTM48R_N_x_x_x_015_049_099F_20240510T014706_20240510T014727_PIC0_01.tif
path_tif_wgs84=data/dianchi_test/SWOT_L2_HR_Raster_100m_UTM48R_N_x_x_x_015_049_099F_20240510T014706_20240510T014727_PIC0_01_wgs84.tif

# gdalmdimtranslate \
#   -of "GTiff" \
#   -array "wse" \
#   -co "COMPRESS=LZW" $path_nc $path_tif

gdalwarp -overwrite \
  -s_srs EPSG:32648 \
  -t_srs EPSG:4326 \
  -r cubic \
  -co COMPRESS=LZW \
  -co TILED=YES \
  $path_tif $path_tif_wgs84



