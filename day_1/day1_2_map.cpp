#include <iostream>
#include <unordered_map>
#include "day1_data.h"

/* Tried to optimise the challenge with C++ solution, still only about twice as fast
 * as the python solution as this is a case where knowing your data structures and
 * their complexity makes all the difference.
 *
 * Interestingly enough, std::unordered_map (which is implemented as a hash map)
 * is the only one that can compete with the python implementation. The performance
 * using std::map (which usually is a red black tree) is about the same as for the
 * python solution.
 *
 * compile with: g++ --std=c++17 -Wall -O3 day1_2_map.cpp -o day1_2_map
 */

int main()
{
    int freq = 0;
    std::unordered_map<int, int> hist;
    hist[freq] = 1;
    while (true)
    {
        for (auto i: DATA)
        {
            freq += i;
            if (hist.find(freq) != hist.end())
            {
                std::cout << "Freq " << freq << " appears twice" << std::endl;
                return 0;
            }
            hist[freq] = 1;
        }
    }
    return -1;
}