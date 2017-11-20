#----------------------------------------------------------------
# Generated CMake target import file for configuration "None".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "opencv_core" for configuration "None"
set_property(TARGET opencv_core APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_core PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE ""
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_core.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_core.so.3.3.1"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_core )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_core "${_IMPORT_PREFIX}/lib/libopencv_core.so.3.3.1" )

# Import target "opencv_flann" for configuration "None"
set_property(TARGET opencv_flann APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_flann PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_flann.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_flann.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_flann )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_flann "${_IMPORT_PREFIX}/lib/libopencv_flann.so.3.3.1" )

# Import target "opencv_hdf" for configuration "None"
set_property(TARGET opencv_hdf APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_hdf PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_hdf.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_hdf.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_hdf )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_hdf "${_IMPORT_PREFIX}/lib/libopencv_hdf.so.3.3.1" )

# Import target "opencv_imgproc" for configuration "None"
set_property(TARGET opencv_imgproc APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_imgproc PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_imgproc.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_imgproc.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_imgproc )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_imgproc "${_IMPORT_PREFIX}/lib/libopencv_imgproc.so.3.3.1" )

# Import target "opencv_ml" for configuration "None"
set_property(TARGET opencv_ml APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_ml PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_ml.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_ml.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_ml )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_ml "${_IMPORT_PREFIX}/lib/libopencv_ml.so.3.3.1" )

# Import target "opencv_photo" for configuration "None"
set_property(TARGET opencv_photo APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_photo PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core;opencv_imgproc"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_photo.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_photo.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_photo )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_photo "${_IMPORT_PREFIX}/lib/libopencv_photo.so.3.3.1" )

# Import target "opencv_reg" for configuration "None"
set_property(TARGET opencv_reg APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_reg PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core;opencv_imgproc"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_reg.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_reg.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_reg )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_reg "${_IMPORT_PREFIX}/lib/libopencv_reg.so.3.3.1" )

# Import target "opencv_surface_matching" for configuration "None"
set_property(TARGET opencv_surface_matching APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_surface_matching PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core;opencv_flann"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_surface_matching.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_surface_matching.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_surface_matching )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_surface_matching "${_IMPORT_PREFIX}/lib/libopencv_surface_matching.so.3.3.1" )

# Import target "opencv_video" for configuration "None"
set_property(TARGET opencv_video APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_video PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core;opencv_imgproc"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_video.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_video.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_video )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_video "${_IMPORT_PREFIX}/lib/libopencv_video.so.3.3.1" )

# Import target "opencv_viz" for configuration "None"
set_property(TARGET opencv_viz APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_viz PROPERTIES
  IMPORTED_LINK_DEPENDENT_LIBRARIES_NONE "vtkRenderingOpenGL;vtkImagingHybrid;vtkIOImage;vtkCommonDataModel;vtkCommonMath;vtkCommonCore;vtksys;vtkCommonMisc;vtkCommonSystem;vtkCommonTransforms;vtkCommonExecutionModel;vtkDICOMParser;vtkIOCore;vtkmetaio;vtkImagingCore;vtkRenderingCore;vtkCommonColor;vtkFiltersExtraction;vtkFiltersCore;vtkFiltersGeneral;vtkCommonComputationalGeometry;vtkFiltersStatistics;vtkImagingFourier;vtkalglib;vtkFiltersGeometry;vtkFiltersSources;vtkInteractionStyle;vtkRenderingLOD;vtkFiltersModeling;vtkIOPLY;vtkIOGeometry;vtkFiltersTexture;vtkRenderingFreeType;vtkftgl;vtkIOExport;vtkRenderingAnnotation;vtkImagingColor;vtkRenderingContext2D;vtkRenderingGL2PS;vtkRenderingContextOpenGL;vtkRenderingLabel"
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_viz.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_viz.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_viz )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_viz "${_IMPORT_PREFIX}/lib/libopencv_viz.so.3.3.1" )

# Import target "opencv_fuzzy" for configuration "None"
set_property(TARGET opencv_fuzzy APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_fuzzy PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core;opencv_imgproc"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_fuzzy.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_fuzzy.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_fuzzy )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_fuzzy "${_IMPORT_PREFIX}/lib/libopencv_fuzzy.so.3.3.1" )

# Import target "opencv_imgcodecs" for configuration "None"
set_property(TARGET opencv_imgcodecs APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_imgcodecs PROPERTIES
  IMPORTED_LINK_DEPENDENT_LIBRARIES_NONE "opencv_core;opencv_imgproc"
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE ""
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_imgcodecs.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_imgcodecs.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_imgcodecs )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_imgcodecs "${_IMPORT_PREFIX}/lib/libopencv_imgcodecs.so.3.3.1" )

# Import target "opencv_shape" for configuration "None"
set_property(TARGET opencv_shape APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_shape PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core;opencv_imgproc;opencv_video"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_shape.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_shape.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_shape )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_shape "${_IMPORT_PREFIX}/lib/libopencv_shape.so.3.3.1" )

# Import target "opencv_videoio" for configuration "None"
set_property(TARGET opencv_videoio APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_videoio PROPERTIES
  IMPORTED_LINK_DEPENDENT_LIBRARIES_NONE "opencv_core;opencv_imgproc;opencv_imgcodecs"
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE ""
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_videoio.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_videoio.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_videoio )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_videoio "${_IMPORT_PREFIX}/lib/libopencv_videoio.so.3.3.1" )

# Import target "opencv_highgui" for configuration "None"
set_property(TARGET opencv_highgui APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_highgui PROPERTIES
  IMPORTED_LINK_DEPENDENT_LIBRARIES_NONE "opencv_core;opencv_imgproc;opencv_imgcodecs;opencv_videoio;Qt5::Core;Qt5::Gui;Qt5::Widgets;Qt5::Test;Qt5::Concurrent"
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE ""
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_highgui.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_highgui.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_highgui )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_highgui "${_IMPORT_PREFIX}/lib/libopencv_highgui.so.3.3.1" )

# Import target "opencv_objdetect" for configuration "None"
set_property(TARGET opencv_objdetect APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_objdetect PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core;opencv_imgproc;opencv_ml;opencv_imgcodecs;opencv_videoio;opencv_highgui"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_objdetect.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_objdetect.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_objdetect )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_objdetect "${_IMPORT_PREFIX}/lib/libopencv_objdetect.so.3.3.1" )

# Import target "opencv_plot" for configuration "None"
set_property(TARGET opencv_plot APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_plot PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core;opencv_imgproc;opencv_imgcodecs;opencv_videoio;opencv_highgui"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_plot.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_plot.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_plot )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_plot "${_IMPORT_PREFIX}/lib/libopencv_plot.so.3.3.1" )

# Import target "opencv_superres" for configuration "None"
set_property(TARGET opencv_superres APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_superres PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core;opencv_imgproc;opencv_video;opencv_imgcodecs;opencv_videoio"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_superres.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_superres.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_superres )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_superres "${_IMPORT_PREFIX}/lib/libopencv_superres.so.3.3.1" )

# Import target "opencv_xobjdetect" for configuration "None"
set_property(TARGET opencv_xobjdetect APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_xobjdetect PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core;opencv_imgproc;opencv_ml;opencv_imgcodecs;opencv_videoio;opencv_highgui;opencv_objdetect"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_xobjdetect.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_xobjdetect.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_xobjdetect )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_xobjdetect "${_IMPORT_PREFIX}/lib/libopencv_xobjdetect.so.3.3.1" )

# Import target "opencv_xphoto" for configuration "None"
set_property(TARGET opencv_xphoto APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_xphoto PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core;opencv_imgproc;opencv_photo;opencv_imgcodecs;opencv_videoio;opencv_highgui"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_xphoto.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_xphoto.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_xphoto )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_xphoto "${_IMPORT_PREFIX}/lib/libopencv_xphoto.so.3.3.1" )

# Import target "opencv_bgsegm" for configuration "None"
set_property(TARGET opencv_bgsegm APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_bgsegm PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core;opencv_imgproc;opencv_video;opencv_imgcodecs;opencv_videoio;opencv_highgui"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_bgsegm.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_bgsegm.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_bgsegm )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_bgsegm "${_IMPORT_PREFIX}/lib/libopencv_bgsegm.so.3.3.1" )

# Import target "opencv_bioinspired" for configuration "None"
set_property(TARGET opencv_bioinspired APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_bioinspired PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core;opencv_imgproc;opencv_imgcodecs;opencv_videoio;opencv_highgui"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_bioinspired.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_bioinspired.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_bioinspired )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_bioinspired "${_IMPORT_PREFIX}/lib/libopencv_bioinspired.so.3.3.1" )

# Import target "opencv_dpm" for configuration "None"
set_property(TARGET opencv_dpm APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_dpm PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core;opencv_imgproc;opencv_ml;opencv_imgcodecs;opencv_videoio;opencv_highgui;opencv_objdetect"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_dpm.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_dpm.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_dpm )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_dpm "${_IMPORT_PREFIX}/lib/libopencv_dpm.so.3.3.1" )

# Import target "opencv_face" for configuration "None"
set_property(TARGET opencv_face APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_face PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core;opencv_imgproc;opencv_ml;opencv_imgcodecs;opencv_videoio;opencv_highgui;opencv_objdetect"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_face.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_face.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_face )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_face "${_IMPORT_PREFIX}/lib/libopencv_face.so.3.3.1" )

# Import target "opencv_features2d" for configuration "None"
set_property(TARGET opencv_features2d APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_features2d PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core;opencv_flann;opencv_imgproc;opencv_ml;opencv_imgcodecs;opencv_videoio;opencv_highgui"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_features2d.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_features2d.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_features2d )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_features2d "${_IMPORT_PREFIX}/lib/libopencv_features2d.so.3.3.1" )

# Import target "opencv_line_descriptor" for configuration "None"
set_property(TARGET opencv_line_descriptor APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_line_descriptor PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core;opencv_flann;opencv_imgproc;opencv_ml;opencv_imgcodecs;opencv_videoio;opencv_highgui;opencv_features2d"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_line_descriptor.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_line_descriptor.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_line_descriptor )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_line_descriptor "${_IMPORT_PREFIX}/lib/libopencv_line_descriptor.so.3.3.1" )

# Import target "opencv_saliency" for configuration "None"
set_property(TARGET opencv_saliency APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_saliency PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core;opencv_flann;opencv_imgproc;opencv_ml;opencv_imgcodecs;opencv_videoio;opencv_highgui;opencv_features2d"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_saliency.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_saliency.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_saliency )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_saliency "${_IMPORT_PREFIX}/lib/libopencv_saliency.so.3.3.1" )

# Import target "opencv_text" for configuration "None"
set_property(TARGET opencv_text APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_text PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core;opencv_flann;opencv_imgproc;opencv_ml;opencv_imgcodecs;opencv_videoio;opencv_highgui;opencv_features2d"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_text.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_text.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_text )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_text "${_IMPORT_PREFIX}/lib/libopencv_text.so.3.3.1" )

# Import target "opencv_calib3d" for configuration "None"
set_property(TARGET opencv_calib3d APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_calib3d PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core;opencv_flann;opencv_imgproc;opencv_ml;opencv_imgcodecs;opencv_videoio;opencv_highgui;opencv_features2d"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_calib3d.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_calib3d.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_calib3d )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_calib3d "${_IMPORT_PREFIX}/lib/libopencv_calib3d.so.3.3.1" )

# Import target "opencv_ccalib" for configuration "None"
set_property(TARGET opencv_ccalib APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_ccalib PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core;opencv_flann;opencv_imgproc;opencv_ml;opencv_imgcodecs;opencv_videoio;opencv_highgui;opencv_features2d;opencv_calib3d"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_ccalib.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_ccalib.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_ccalib )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_ccalib "${_IMPORT_PREFIX}/lib/libopencv_ccalib.so.3.3.1" )

# Import target "opencv_cvv" for configuration "None"
set_property(TARGET opencv_cvv APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_cvv PROPERTIES
  IMPORTED_LINK_DEPENDENT_LIBRARIES_NONE "Qt5::Core;Qt5::Gui;Qt5::Widgets"
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core;opencv_flann;opencv_imgproc;opencv_ml;opencv_imgcodecs;opencv_videoio;opencv_highgui;opencv_features2d"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_cvv.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_cvv.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_cvv )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_cvv "${_IMPORT_PREFIX}/lib/libopencv_cvv.so.3.3.1" )

# Import target "opencv_datasets" for configuration "None"
set_property(TARGET opencv_datasets APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_datasets PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core;opencv_flann;opencv_imgproc;opencv_ml;opencv_imgcodecs;opencv_videoio;opencv_highgui;opencv_objdetect;opencv_face;opencv_features2d;opencv_text"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_datasets.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_datasets.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_datasets )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_datasets "${_IMPORT_PREFIX}/lib/libopencv_datasets.so.3.3.1" )

# Import target "opencv_rgbd" for configuration "None"
set_property(TARGET opencv_rgbd APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_rgbd PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core;opencv_flann;opencv_imgproc;opencv_ml;opencv_imgcodecs;opencv_videoio;opencv_highgui;opencv_features2d;opencv_calib3d"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_rgbd.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_rgbd.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_rgbd )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_rgbd "${_IMPORT_PREFIX}/lib/libopencv_rgbd.so.3.3.1" )

# Import target "opencv_stereo" for configuration "None"
set_property(TARGET opencv_stereo APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_stereo PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core;opencv_flann;opencv_imgproc;opencv_ml;opencv_imgcodecs;opencv_videoio;opencv_highgui;opencv_features2d;opencv_calib3d"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_stereo.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_stereo.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_stereo )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_stereo "${_IMPORT_PREFIX}/lib/libopencv_stereo.so.3.3.1" )

# Import target "opencv_videostab" for configuration "None"
set_property(TARGET opencv_videostab APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_videostab PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core;opencv_flann;opencv_imgproc;opencv_ml;opencv_photo;opencv_video;opencv_imgcodecs;opencv_videoio;opencv_highgui;opencv_features2d;opencv_calib3d"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_videostab.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_videostab.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_videostab )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_videostab "${_IMPORT_PREFIX}/lib/libopencv_videostab.so.3.3.1" )

# Import target "opencv_xfeatures2d" for configuration "None"
set_property(TARGET opencv_xfeatures2d APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_xfeatures2d PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core;opencv_flann;opencv_imgproc;opencv_ml;opencv_video;opencv_imgcodecs;opencv_shape;opencv_videoio;opencv_highgui;opencv_features2d;opencv_calib3d"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_xfeatures2d.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_xfeatures2d.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_xfeatures2d )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_xfeatures2d "${_IMPORT_PREFIX}/lib/libopencv_xfeatures2d.so.3.3.1" )

# Import target "opencv_ximgproc" for configuration "None"
set_property(TARGET opencv_ximgproc APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_ximgproc PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core;opencv_flann;opencv_imgproc;opencv_ml;opencv_imgcodecs;opencv_videoio;opencv_highgui;opencv_features2d;opencv_calib3d"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_ximgproc.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_ximgproc.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_ximgproc )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_ximgproc "${_IMPORT_PREFIX}/lib/libopencv_ximgproc.so.3.3.1" )

# Import target "opencv_aruco" for configuration "None"
set_property(TARGET opencv_aruco APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_aruco PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core;opencv_flann;opencv_imgproc;opencv_ml;opencv_imgcodecs;opencv_videoio;opencv_highgui;opencv_features2d;opencv_calib3d"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_aruco.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_aruco.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_aruco )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_aruco "${_IMPORT_PREFIX}/lib/libopencv_aruco.so.3.3.1" )

# Import target "opencv_optflow" for configuration "None"
set_property(TARGET opencv_optflow APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_optflow PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core;opencv_flann;opencv_imgproc;opencv_ml;opencv_video;opencv_imgcodecs;opencv_videoio;opencv_highgui;opencv_features2d;opencv_calib3d;opencv_ximgproc"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_optflow.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_optflow.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_optflow )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_optflow "${_IMPORT_PREFIX}/lib/libopencv_optflow.so.3.3.1" )

# Import target "opencv_phase_unwrapping" for configuration "None"
set_property(TARGET opencv_phase_unwrapping APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_phase_unwrapping PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core;opencv_flann;opencv_imgproc;opencv_ml;opencv_imgcodecs;opencv_videoio;opencv_highgui;opencv_features2d;opencv_calib3d;opencv_rgbd"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_phase_unwrapping.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_phase_unwrapping.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_phase_unwrapping )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_phase_unwrapping "${_IMPORT_PREFIX}/lib/libopencv_phase_unwrapping.so.3.3.1" )

# Import target "opencv_stitching" for configuration "None"
set_property(TARGET opencv_stitching APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_stitching PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core;opencv_flann;opencv_imgproc;opencv_ml;opencv_video;opencv_imgcodecs;opencv_shape;opencv_videoio;opencv_highgui;opencv_objdetect;opencv_features2d;opencv_calib3d;opencv_xfeatures2d"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_stitching.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_stitching.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_stitching )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_stitching "${_IMPORT_PREFIX}/lib/libopencv_stitching.so.3.3.1" )

# Import target "opencv_structured_light" for configuration "None"
set_property(TARGET opencv_structured_light APPEND PROPERTY IMPORTED_CONFIGURATIONS NONE)
set_target_properties(opencv_structured_light PROPERTIES
  IMPORTED_LINK_DEPENDENT_LIBRARIES_NONE "vtkRenderingOpenGL;vtkImagingHybrid;vtkIOImage;vtkCommonDataModel;vtkCommonMath;vtkCommonCore;vtksys;vtkCommonMisc;vtkCommonSystem;vtkCommonTransforms;vtkCommonExecutionModel;vtkDICOMParser;vtkIOCore;vtkmetaio;vtkImagingCore;vtkRenderingCore;vtkCommonColor;vtkFiltersExtraction;vtkFiltersCore;vtkFiltersGeneral;vtkCommonComputationalGeometry;vtkFiltersStatistics;vtkImagingFourier;vtkalglib;vtkFiltersGeometry;vtkFiltersSources;vtkInteractionStyle;vtkRenderingLOD;vtkFiltersModeling;vtkIOPLY;vtkIOGeometry;vtkFiltersTexture;vtkRenderingFreeType;vtkftgl;vtkIOExport;vtkRenderingAnnotation;vtkImagingColor;vtkRenderingContext2D;vtkRenderingGL2PS;vtkRenderingContextOpenGL;vtkRenderingLabel"
  IMPORTED_LINK_INTERFACE_LIBRARIES_NONE "opencv_core;opencv_flann;opencv_imgproc;opencv_ml;opencv_viz;opencv_imgcodecs;opencv_videoio;opencv_highgui;opencv_features2d;opencv_calib3d;opencv_rgbd;opencv_phase_unwrapping"
  IMPORTED_LOCATION_NONE "${_IMPORT_PREFIX}/lib/libopencv_structured_light.so.3.3.1"
  IMPORTED_SONAME_NONE "libopencv_structured_light.so.3.3"
  )

list(APPEND _IMPORT_CHECK_TARGETS opencv_structured_light )
list(APPEND _IMPORT_CHECK_FILES_FOR_opencv_structured_light "${_IMPORT_PREFIX}/lib/libopencv_structured_light.so.3.3.1" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)