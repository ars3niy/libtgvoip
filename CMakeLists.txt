set(NoPkgConfig FALSE CACHE BOOL "Do not use pkcconfig")

if (NOT NoPkgConfig)
    include(FindPkgConfig)
    pkg_check_modules(opus REQUIRED opus)
    pkg_check_modules(webrtc_audio REQUIRED webrtc-audio-processing)
endif (NOT NoPkgConfig)

set(WithPulse FALSE CACHE BOOL "Build with pulseaudio")
set(WithAlsa TRUE CACHE BOOL "Build wiht ALSA")
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

add_library(tgvoip
    Buffers.cpp
    PacketReassembler.cpp
    VoIPGroupController.cpp
    EchoCanceller.cpp
    NetworkSocket.cpp
    OpusDecoder.cpp
    OpusEncoder.cpp
    BlockingQueue.cpp
    JitterBuffer.cpp
    MediaStreamItf.cpp
    audio/AudioIOCallback.cpp
    audio/Resampler.cpp
    audio/AudioInput.cpp
    audio/AudioOutput.cpp
    audio/AudioIO.cpp
    json11.cpp
    VoIPController.cpp
    logging.cpp
    MessageThread.cpp
    CongestionControl.cpp
    video/VideoPacketSender.cpp
    video/ScreamCongestionController.cpp
    video/VideoSource.cpp
    video/VideoRenderer.cpp
    video/VideoFEC.cpp
    #video/cm256/cm256.cpp
    #video/cm256/gf256.cpp
    VoIPServerConfig.cpp
)

if (NOT WIN32)
    if (WithPulse)
        target_sources(tgvoip PRIVATE
            os/linux/AudioPulse.cpp
            os/linux/AudioOutputPulse.cpp
            os/linux/AudioInputPulse.cpp
        )
    else (WithPulse)
        target_compile_definitions(tgvoip PRIVATE WITHOUT_PULSE)
    endif (WithPulse)

    if (WithAlsa)
        target_sources(tgvoip PRIVATE
            os/linux/AudioOutputALSA.cpp
            os/linux/AudioInputALSA.cpp
        )
    else (WithAlsa)
        target_compile_definitions(tgvoip PRIVATE WITHOUT_ALSA)
    endif (WithAlsa)

    target_sources(tgvoip PRIVATE
        os/posix/NetworkSocketPosix.cpp
    )
endif (NOT WIN32)

if (WIN32)
    target_sources(tgvoip PRIVATE
        os/windows/AudioInputWave.cpp
        os/windows/AudioOutputWave.cpp
        os/windows/NetworkSocketWinsock.cpp
        os/windows/AudioInputWASAPI.cpp
        os/windows/WindowsSpecific.cpp
        os/windows/AudioOutputWASAPI.cpp
    )
endif (WIN32)

target_include_directories(tgvoip PRIVATE webrtc_dsp ${opus_INCLUDE_DIRS})
target_compile_options(tgvoip PRIVATE ${webrtc_audio_CFLAGS})

if (NOT DEFINED CMAKE_INSTALL_LIBDIR)
  set(CMAKE_INSTALL_LIBDIR "lib")
endif()
if (NOT DEFINED CMAKE_INSTALL_INCLUDEDIR)
  set(CMAKE_INSTALL_INCLUDEDIR "include")
endif()

install(TARGETS tgvoip ARCHIVE DESTINATION "${CMAKE_INSTALL_LIBDIR}" LIBRARY DESTINATION "${CMAKE_INSTALL_LIBDIR}")

install(FILES 
    NetworkSocket.h
    VoIPController.h
    MediaStreamItf.h
    BlockingQueue.h
    MessageThread.h
    tests/MockReflector.h
    threading.h
    OpusDecoder.h
    logging.h
    PacketReassembler.h
    EchoCanceller.h
    VoIPServerConfig.h
    Buffers.h
    utils.h
    JitterBuffer.h
    #PacketSender.h
    PrivateDefines.h
    OpusEncoder.h
    CongestionControl.h
    DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}/tgvoip"
)

install(FILES 
    audio/AudioInput.h
    audio/Resampler.h
    audio/AudioIO.h
    audio/AudioIOCallback.h
    audio/AudioOutput.h
    DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}/tgvoip/audio"
)

install(FILES 
    video/VideoSource.h
    video/VideoRenderer.h
    #video/VideoPacketSender.h
    video/ScreamCongestionController.h
    #video/VideoFEC.h
    DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}/tgvoip/video"
)
