//code from www.361way.com
#include<iostream>
#include<fstream>
#include<cstdlib>
#include<sstream>

using namespace std;

//struct: Property of a tcp connection
struct ConnectionProperty
{
    string local_addr;
    string remote_addr;
    string state;
};

//Change hexadecimal number to decimal number
int HexToInt(char h)
{
    if(h >= '0' && h <= '9')
    {
        return h - '0';
    }
    else if(h >= 'A' && h <= 'F')
    {
        return h - 'A' + 10;
    }
    else
    {
        cerr << "Error: Illegal Hex Number!" << endl;
        return -1;
    }
}

//Get Ip address and port number from string XXXXXXXX:XXXX
string GetIpAddress(char* str)
{
    int a, b, c, d, e;

    a = HexToInt(str[0]) * 16 + HexToInt(str[1]);
    b = HexToInt(str[2]) * 16 + HexToInt(str[3]);
    c = HexToInt(str[4]) * 16 + HexToInt(str[5]);
    d = HexToInt(str[6]) * 16 + HexToInt(str[7]);
    e = HexToInt(str[9]) * 16 * 16 * 16 +
        HexToInt(str[10]) * 16 * 16 +
        HexToInt(str[11]) * 16 +
        HexToInt(str[12]);

    //change int to string
    string sa, sb, sc, sd, se;
    ostringstream oss;
    oss << a;
    sa = oss.str();
    oss.str(""); //clear the content in oss
    oss << b;
    sb = oss.str();
    oss.str("");
    oss << c;
    sc = oss.str();
    oss.str("");
    oss << d;
    sd = oss.str();
    oss.str("");
    oss << e;
    se = oss.str();
    oss.str("");

    //return by order: d.c.b.a:e
    return sd + '.' + sc + '.' + sb + '.' + sa + ':' + se;
}

//Get tcp connection state
string GetConnectionState(char* str)
{

    if(str[0] == '0' && str[1] == '0') return "ERROR_STATUS";
    if(str[0] == '0' && str[1] == '1') return "TCP_ESTABLISHED";
    if(str[0] == '0' && str[1] == '2') return "TCP_SYN_SENT";
    if(str[0] == '0' && str[1] == '3') return "TCP_SYN_RECV";
    if(str[0] == '0' && str[1] == '4') return "TCP_FIN_WAIT1";
    if(str[0] == '0' && str[1] == '5') return "TCP_FIN_WAIT2";
    if(str[0] == '0' && str[1] == '6') return "TCP_TIME_WAIT";
    if(str[0] == '0' && str[1] == '7') return "TCP_CLOSE";
    if(str[0] == '0' && str[1] == '8') return "TCP_CLOSE_WAIT";
    if(str[0] == '0' && str[1] == '9') return "TCP_LAST_ACK";
    if(str[0] == '0' && str[1] == 'A') return "TCP_LISTEN";
    if(str[0] == '0' && str[1] == 'B') return "TCP_CLOSING";
    return "UNKNOWN_STATE";
}

int main()
{
    //read from file /proc/net/tcp
    ifstream infile("/proc/net/tcp", ios :: in);
    if(!infile)
    {
        cerr << "open error!" << endl;
        exit(1);
    }

    string s;
    char s_local_addr[20], s_remote_addr[20], s_state[20];
    getline(infile, s); //title: every column's name
    while(getline(infile, s))
    {
        sscanf(s.c_str(), "%*s%s%s%s", s_local_addr, s_remote_addr, s_state);
        //printf("%s\t%s\t%s\n", s_local_addr, s_remote_addr, s_state);

        string ip_local = GetIpAddress(s_local_addr);
        string ip_remote = GetIpAddress(s_remote_addr);
        string conn_state = GetConnectionState(s_state);

        cout << ip_local << "\t" << ip_remote << "\t" << conn_state << endl;
    }

    return 0;
}
