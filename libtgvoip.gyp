# GYP project file for TDesktop

{
    'targets': [
      {
        'target_name': 'libtgvoip',
        'type': 'static_library',
        'dependencies': [],
        'defines': [
          'TGVOIP_USE_DESKTOP_DSP',
          'WEBRTC_AUDIO_PROCESSING_ONLY_BUILD'
        ],
        'variables': {
          'without_pulse%': 0,
          'without_alsa%': 0,
          'tgvoip_src_loc': '.',
          'official_build_target%': '',
          'linux_path_opus_include%': '<(DEPTH)/../../../Libraries/opus/include',
          'webrtc_include%': '',
          'dynamic_msvc_runtime%': 0,
        },
        'include_dirs': [
          '<(webrtc_include)',
          '<(linux_path_opus_include)',
        ],
        'direct_dependent_settings': {
          'include_dirs': [
            '<(tgvoip_src_loc)',
          ],
        },
        'export_dependent_settings': [],
        'sources': [
          '<(tgvoip_src_loc)/BlockingQueue.cpp',
          '<(tgvoip_src_loc)/BlockingQueue.h',
          '<(tgvoip_src_loc)/Buffers.cpp',
          '<(tgvoip_src_loc)/Buffers.h',
          '<(tgvoip_src_loc)/CongestionControl.cpp',
          '<(tgvoip_src_loc)/CongestionControl.h',
          '<(tgvoip_src_loc)/EchoCanceller.cpp',
          '<(tgvoip_src_loc)/EchoCanceller.h',
          '<(tgvoip_src_loc)/JitterBuffer.cpp',
          '<(tgvoip_src_loc)/JitterBuffer.h',
          '<(tgvoip_src_loc)/logging.cpp',
          '<(tgvoip_src_loc)/logging.h',
          '<(tgvoip_src_loc)/MediaStreamItf.cpp',
          '<(tgvoip_src_loc)/MediaStreamItf.h',
          '<(tgvoip_src_loc)/OpusDecoder.cpp',
          '<(tgvoip_src_loc)/OpusDecoder.h',
          '<(tgvoip_src_loc)/OpusEncoder.cpp',
          '<(tgvoip_src_loc)/OpusEncoder.h',
          '<(tgvoip_src_loc)/threading.h',
          '<(tgvoip_src_loc)/VoIPController.cpp',
          '<(tgvoip_src_loc)/VoIPGroupController.cpp',
          '<(tgvoip_src_loc)/VoIPController.h',
          '<(tgvoip_src_loc)/PrivateDefines.h',
          '<(tgvoip_src_loc)/VoIPServerConfig.cpp',
          '<(tgvoip_src_loc)/VoIPServerConfig.h',
          '<(tgvoip_src_loc)/audio/AudioInput.cpp',
          '<(tgvoip_src_loc)/audio/AudioInput.h',
          '<(tgvoip_src_loc)/audio/AudioOutput.cpp',
          '<(tgvoip_src_loc)/audio/AudioOutput.h',
          '<(tgvoip_src_loc)/audio/Resampler.cpp',
          '<(tgvoip_src_loc)/audio/Resampler.h',
          '<(tgvoip_src_loc)/NetworkSocket.cpp',
          '<(tgvoip_src_loc)/NetworkSocket.h',
          '<(tgvoip_src_loc)/PacketReassembler.cpp',
          '<(tgvoip_src_loc)/PacketReassembler.h',
          '<(tgvoip_src_loc)/MessageThread.cpp',
          '<(tgvoip_src_loc)/MessageThread.h',
          '<(tgvoip_src_loc)/audio/AudioIO.cpp',
          '<(tgvoip_src_loc)/audio/AudioIO.h',
          '<(tgvoip_src_loc)/audio/AudioIOCallback.cpp',
          '<(tgvoip_src_loc)/audio/AudioIOCallback.h',
          '<(tgvoip_src_loc)/video/ScreamCongestionController.cpp',
          '<(tgvoip_src_loc)/video/ScreamCongestionController.h',
          '<(tgvoip_src_loc)/video/VideoSource.cpp',
          '<(tgvoip_src_loc)/video/VideoSource.h',
          '<(tgvoip_src_loc)/video/VideoRenderer.cpp',
          '<(tgvoip_src_loc)/video/VideoRenderer.h',
          '<(tgvoip_src_loc)/video/VideoPacketSender.cpp',
          '<(tgvoip_src_loc)/video/VideoPacketSender.h',
          '<(tgvoip_src_loc)/video/VideoFEC.cpp',
          '<(tgvoip_src_loc)/video/VideoFEC.h',
          '<(tgvoip_src_loc)/json11.cpp',
          '<(tgvoip_src_loc)/json11.hpp',

          # Windows
          '<(tgvoip_src_loc)/os/windows/NetworkSocketWinsock.cpp',
          '<(tgvoip_src_loc)/os/windows/NetworkSocketWinsock.h',
          '<(tgvoip_src_loc)/os/windows/AudioInputWave.cpp',
          '<(tgvoip_src_loc)/os/windows/AudioInputWave.h',
          '<(tgvoip_src_loc)/os/windows/AudioOutputWave.cpp',
          '<(tgvoip_src_loc)/os/windows/AudioOutputWave.h',
          '<(tgvoip_src_loc)/os/windows/AudioOutputWASAPI.cpp',
          '<(tgvoip_src_loc)/os/windows/AudioOutputWASAPI.h',
          '<(tgvoip_src_loc)/os/windows/AudioInputWASAPI.cpp',
          '<(tgvoip_src_loc)/os/windows/AudioInputWASAPI.h',
          '<(tgvoip_src_loc)/os/windows/WindowsSpecific.cpp',
          '<(tgvoip_src_loc)/os/windows/WindowsSpecific.h',

          # macOS
          '<(tgvoip_src_loc)/os/darwin/AudioInputAudioUnit.cpp',
          '<(tgvoip_src_loc)/os/darwin/AudioInputAudioUnit.h',
          '<(tgvoip_src_loc)/os/darwin/AudioOutputAudioUnit.cpp',
          '<(tgvoip_src_loc)/os/darwin/AudioOutputAudioUnit.h',
          '<(tgvoip_src_loc)/os/darwin/AudioInputAudioUnitOSX.cpp',
          '<(tgvoip_src_loc)/os/darwin/AudioInputAudioUnitOSX.h',
          '<(tgvoip_src_loc)/os/darwin/AudioOutputAudioUnitOSX.cpp',
          '<(tgvoip_src_loc)/os/darwin/AudioOutputAudioUnitOSX.h',
          '<(tgvoip_src_loc)/os/darwin/AudioUnitIO.cpp',
          '<(tgvoip_src_loc)/os/darwin/AudioUnitIO.h',
          '<(tgvoip_src_loc)/os/darwin/DarwinSpecific.mm',
          '<(tgvoip_src_loc)/os/darwin/DarwinSpecific.h',

          # Linux
          '<(tgvoip_src_loc)/os/linux/AudioInputALSA.cpp',
          '<(tgvoip_src_loc)/os/linux/AudioInputALSA.h',
          '<(tgvoip_src_loc)/os/linux/AudioOutputALSA.cpp',
          '<(tgvoip_src_loc)/os/linux/AudioOutputALSA.h',
          '<(tgvoip_src_loc)/os/linux/AudioOutputPulse.cpp',
          '<(tgvoip_src_loc)/os/linux/AudioOutputPulse.h',
          '<(tgvoip_src_loc)/os/linux/AudioInputPulse.cpp',
          '<(tgvoip_src_loc)/os/linux/AudioInputPulse.h',
          '<(tgvoip_src_loc)/os/linux/AudioPulse.cpp',
          '<(tgvoip_src_loc)/os/linux/AudioPulse.h',

          # POSIX
          '<(tgvoip_src_loc)/os/posix/NetworkSocketPosix.cpp',
          '<(tgvoip_src_loc)/os/posix/NetworkSocketPosix.h',

        ],
        'libraries': [],
        'configurations': {
          'Debug': {},
          'Release': {},
        },
        'conditions': [
          [
            '"<(OS)" != "win"', {
              'sources/': [['exclude', '<(tgvoip_src_loc)/os/windows/']],
            }, {
              'sources/': [['exclude', '<(tgvoip_src_loc)/os/posix/']],
            },
          ],
          [
            '"<(OS)" != "mac"', {
              'sources/': [['exclude', '<(tgvoip_src_loc)/os/darwin/']],
            },
          ],
          [
            '"<(OS)" != "linux"', {
              'sources/': [['exclude', '<(tgvoip_src_loc)/os/linux/']],
            },
          ],
          [
            '"<(OS)" == "mac"', {
              'xcode_settings': {
                'CLANG_CXX_LANGUAGE_STANDARD': 'c++11',
                'ALWAYS_SEARCH_USER_PATHS': 'NO',
              },
              'defines': [
                'WEBRTC_POSIX',
                'TARGET_OS_OSX',
              ],
              'sources': [
                '<(tgvoip_src_loc)/webrtc_dsp/rtc_base/logging_mac.mm',
                '<(tgvoip_src_loc)/webrtc_dsp/rtc_base/logging_mac.h',
              ],
              'conditions': [
                [ '"<(official_build_target)" == "mac32"', {
                  'xcode_settings': {
                    'MACOSX_DEPLOYMENT_TARGET': '10.6',
                    'OTHER_CPLUSPLUSFLAGS': [ '-nostdinc++' ],
                  },
                  'include_dirs': [
                    '/usr/local/macold/include/c++/v1',
                    '<(DEPTH)/../../../Libraries/macold/openssl/include',
                  ],
                  'defines': [
                    'TARGET_OSX32',
                  ],
                }, {
                  'xcode_settings': {
                    'MACOSX_DEPLOYMENT_TARGET': '10.8',
                    'CLANG_CXX_LIBRARY': 'libc++',
                  },
                  'include_dirs': [
                    '<(DEPTH)/../../../Libraries/openssl/include',
                  ],
                  'direct_dependent_settings': {
                    'linkflags': [
                      '-framework VideoToolbox',
                    ],
                  },
                  'sources': [
                    '<(tgvoip_src_loc)/os/darwin/TGVVideoRenderer.mm',
                    '<(tgvoip_src_loc)/os/darwin/TGVVideoRenderer.h',
                    '<(tgvoip_src_loc)/os/darwin/TGVVideoSource.mm',
                    '<(tgvoip_src_loc)/os/darwin/TGVVideoSource.h',
                    '<(tgvoip_src_loc)/os/darwin/VideoToolboxEncoderSource.mm',
                    '<(tgvoip_src_loc)/os/darwin/VideoToolboxEncoderSource.h',
                    '<(tgvoip_src_loc)/os/darwin/SampleBufferDisplayLayerRenderer.mm',
                    '<(tgvoip_src_loc)/os/darwin/SampleBufferDisplayLayerRenderer.h',
                  ],
                }],
                ['"<(official_build_target)" == "macstore"', {
                  'defines': [
                    'TGVOIP_NO_OSX_PRIVATE_API',
                  ],
                }],
              ],
            },
          ],
          [
            '"<(OS)" == "win"', {
              'msbuild_toolset': 'v141',
              'defines': [
                'NOMINMAX',
                '_USING_V110_SDK71_',
                'TGVOIP_WINXP_COMPAT',
                'WEBRTC_WIN',
              ],
              'libraries': [
                'winmm',
                'ws2_32',
                'iphlpapi',
                'kernel32',
                'user32',
              ],
              'msvs_cygwin_shell': 0,
              'msvs_settings': {
                'VCCLCompilerTool': {
                  'ProgramDataBaseFileName': '$(OutDir)\\$(ProjectName).pdb',
                  'DebugInformationFormat': '3',  # Program Database (/Zi)
                  'AdditionalOptions': [
                    '/MP',      # Enable multi process build.
                    '/EHsc',    # Catch C++ exceptions only, extern C functions never throw a C++ exception.
                    '/wd4068',  # Disable "warning C4068: unknown pragma"
                  ],
                  'TreatWChar_tAsBuiltInType': 'false',
                },
              },
              'msvs_external_builder_build_cmd': [
                'ninja.exe',
                '-C',
                '$(OutDir)',
                '-k0',
                '$(ProjectName)',
              ],
              'configurations': {
                'Debug': {
                  'defines': [
                    '_DEBUG',
                  ],
                  'include_dirs': [
                    '<(DEPTH)/../../../Libraries/openssl/Debug/include',
                  ],
                  'msvs_settings': {
                    'VCCLCompilerTool': {
                      'Optimization': '0',        # Disabled (/Od)
                      'RuntimeTypeInfo': 'true',

                      'conditions': [
                        [ '<(dynamic_msvc_runtime) == 0', {
                          'RuntimeLibrary': 1,  # Multi-threaded Debug, static (/MTd)
                        }, {
                          'RuntimeLibrary': 3,  # Multi-threaded Debug, dynamic (/MDd)
                        }],
                      ],
                    },
                    'VCLibrarianTool': {
                      'AdditionalOptions': [
                        '/NODEFAULTLIB:LIBCMT',
                      ],
                    },
                  },
                },
                'Release': {
                  'defines': [
                    'NDEBUG',
                  ],
                  'include_dirs': [
                     '<(DEPTH)/../../../Libraries/openssl/Release/include',
                  ],
                  'msvs_settings': {
                    'VCCLCompilerTool': {
                      'Optimization': '2',                  # Maximize Speed (/O2)
                      'InlineFunctionExpansion': '2',       # Any suitable (/Ob2)
                      'EnableIntrinsicFunctions': 'true',   # Yes (/Oi)
                      'FavorSizeOrSpeed': '1',              # Favor fast code (/Ot)
                      'EnableEnhancedInstructionSet': '2',  # Streaming SIMD Extensions 2 (/arch:SSE2)
                      'WholeProgramOptimization': 'true',   # /GL

                      'conditions': [
                        [ '<(dynamic_msvc_runtime) == 0', {
                          'RuntimeLibrary': 0,  # Multi-threaded, static (/MT)
                        }, {
                          'RuntimeLibrary': 2,  # Multi-threaded, dynamic (/MD)
                        }],
                      ],
                    },
                    'VCLibrarianTool': {
                      'AdditionalOptions': [
                        '/LTCG',
                      ],
                    },
                  },
                },
              },
            },
          ],
          [
            '"<(OS)" == "linux"', {
              'defines': [
                'WEBRTC_POSIX',
              ],
              'cflags': [
                '-fPIC -g',
              ],
              'conditions': [
                [ '"<!(uname -m)" == "i686"', {
                  'cflags': [
                    '-msse2',
                  ],
                }],
                [ '"<(without_pulse)" == "1"', {
                  'sources/': [
                    ['exclude', '<(tgvoip_src_loc)/os/linux/AudioInputPulse.cpp'],
                    ['exclude', '<(tgvoip_src_loc)/os/linux/AudioOutputPulse.cpp'],
                    ['exclude', '<(tgvoip_src_loc)/os/linux/AudioPulse.cpp'],
                  ],
                  'defines': [
                    'WITHOUT_PULSE',
                  ],
                }],
                [ '"<(without_alsa)" == "1"', {
                  'sources/': [
                    ['exclude', '<(tgvoip_src_loc)/os/linux/AudioInputALSA.cpp'],
                    ['exclude', '<(tgvoip_src_loc)/os/linux/AudioOutputALSA.cpp'],
                  ],
                  'defines': [
                    'WITHOUT_ALSA',
                  ],
                }],
              ],
              'direct_dependent_settings': {
                'libraries': [

                ],
              },
            },
          ],
        ],
      },
    ],
}
