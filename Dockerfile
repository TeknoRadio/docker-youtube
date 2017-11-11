FROM jrottenberg/ffmpeg:latest
ENV SOURCE_URL="http://relay01.teknoradio.org:9000/128kbps.mp3"
ENV DEST_URL="rtmp://a.rtmp.youtube.com/live2/your-live-streaming-key"
ENV BACKGROUND="/home/user/background.png"
RUN useradd --shell /bin/bash user
ADD config/background.png /home/user/background.png
ADD config/entrypoint.sh /home/user/entrypoint.sh
RUN chown user:nogroup -Rv /home/user && chmod 750 /home/user/entrypoint.sh
USER user:nogroup
WORKDIR /home/user
ENTRYPOINT  ["/home/user/entrypoint.sh"]
