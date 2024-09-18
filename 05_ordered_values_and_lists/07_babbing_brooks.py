# DMOJ problem - ccc00s2
# https://dmoj.ca/problem/ccc00s2


def calculate_streams():
    streams_count = int(input())

    streams = []
    for _ in range(streams_count):
        volume = int(input())
        streams.append(volume)

    while True:
        signal = int(input())
        if signal == 99:
            number = int(input())
            percent = int(input())

            position = int(number - 1)

            left_stream = int(streams[position] * float(percent / 100))
            streams[position] -= left_stream
            streams[position:position] = [left_stream]

        elif signal == 88:
            number = int(input())

            position = int(number - 1)

            streams[position] += streams[position + 1]
            streams.pop(position + 1)
        else:
            break

    str_streams = [str(stream) for stream in streams]
    print(' '.join(str_streams))


calculate_streams()