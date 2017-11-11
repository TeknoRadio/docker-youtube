#!/bin/bash
export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

ffmpeg -re                              \
        -loop 1                         \
        -framerate 2                    \
        -i "${BACKGROUND}"              \
        -i "${SOURCE_URL}"              \
        -c:a aac                        \
        -s 1280x720                     \
        -ab 128k                        \
        -vcodec libx264                 \
        -pix_fmt yuv420p                \
        -maxrate 9500k                  \
        -bufsize 9500k                  \
        -framerate 30                   \
        -g 2                            \
        -strict experimental            \
        -f flv "${DEST_URL}"
