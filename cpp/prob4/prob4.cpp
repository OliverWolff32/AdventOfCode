#include <iostream> 
#include <fstream> 

using namespace std;


int main() {
    ifstream myfile ("OliverProb4Input.txt");
    string line; 
    int nums[4]; 
    int numsLength = 4; 
    int total;
    bool print = true;
    string ch;

    while(getline(myfile, line)) {
        for (int i = 0; i < numsLength; i++) {
            for(int j = 0; j < line.size(); j++) {
                ch += line[j];
                if(ch == "-" || ch == ",") break; 
                nums[i] *= 10; 
                nums[i] += stoi(ch);
                ch = "";
            }
        }
        if(print) {
            for(int i : nums) {
                cout << i << " ";
            }
            cout << endl; 
            print = false;
        }
        
        if(nums[0] >= nums[2] && nums[1] <= nums[3]) total++;
        if(nums[0] < nums[2] && nums[1] > nums[3]) total++;
    }
    cout << total << endl;
    return 0;
}