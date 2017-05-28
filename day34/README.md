Question of the day: https://leetcode.com/problems/validate-ip-address/#/description

Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits. The groups are separated by colons (":"). For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. Also, we could omit some leading zeros among four hexadecimal digits and some low-case characters in the address to upper-case ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a single empty group using two consecutive colons (::) to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For example, the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

Note: You may assume there is no extra space or special characters in the input string.

## Ideas

Distinguishing between IPv4 and IPv6 is easy: one uses '.' and one uses ':' as
the delimeter. Within the IPv4 addresses, the only constraints I need to validate
are that each number between the periods is an integer between 0-255 inclusive,
and that there are no leading 0s.

IPv4  
* '.' delimeter  
* each segement is 0-255  
* no leading 0's  

IPv6 addresses have a little more going on. Each segment is 16 bits, which is
at most 4 digits in hexadecimal. And since they're hexadecimal digits,
letters (a-f) are involved and can be upper case. Leading zero's may or may
not be used, and there are never any empty segments.

IPv6  
* ':' delimeter  
* each segment has at most 4 digits  
* each segment may use letters a, b, c, d, e, f lowercase or capitalized  
* a segment with leading 0's may omit the 0's entirely  
* a segment that contains only 0's may be represented with a single 0, but not as empty  

Input strings that don't fit either set of constraints are neither IPv4 nor IPv6.

This solution basically just parses through the input string a constant number
of times, so it runs in `O(n)` time but because I use the python split
function, it's also using and `O(n)` space.

## Code

[Python](./validateIP.py)

## Follow-up



