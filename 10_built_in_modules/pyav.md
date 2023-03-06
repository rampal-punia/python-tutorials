# Using the pyav library to both read the video stream and then write the processed frames to a new stream

```python
import av

# open the input video stream
input_container = av.open('input.mp4')

# create the output container
output_container = av.open('udp://127.0.0.1:1234', 'w')

# loop through the frames in the input stream
for frame in input_container.decode(video=0):
    # apply object detection on the frame
    # (assuming you have a function called "detect_objects" that takes a frame and returns a processed frame)
    processed_frame = detect_objects(frame)

    # encode the processed frame and write it to the output stream
    packet = output_container.mux(processed_frame)

# close the output container
output_container.close()

```
