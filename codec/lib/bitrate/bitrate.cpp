#include <stdexcept>

unsigned int bitRate(int sampleRate, int bitPrecision, int channels = 1) {
    if (sampleRate <= 0) throw std::invalid_argument("sampleRate must be non-zero positive");
    if (channels <= 0) throw std::invalid_argument("must have at least 1 channel");
    return sampleRate * bitPrecision * channels;
}
