#include <gtest/gtest.h>
#include "../lib/bitrate/bitrate.cpp"

TEST(bitrate, test) {
    EXPECT_EQ(bitRate(1,1,1), 1);
    EXPECT_EQ(bitRate(2,3,4), 24);
    EXPECT_ANY_THROW(bitRate(0,0,0));
    EXPECT_ANY_THROW(bitRate(-1, -1, -1));
}

