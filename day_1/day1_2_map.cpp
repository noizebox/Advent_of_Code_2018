#include <iostream>
#include <unordered_map>
#include "day1_data.h"

/* Tried to optimise it with C++ solution, still only about 50% faster 
 * than the python solution as this is a case where knowing your data 
 * structure makes all the difference.
 
 * compile with: g++ --std=c++17 -Wall -O3 day1_2_map.cpp -o day1_2_map */

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