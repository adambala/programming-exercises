/*
8 kyu: Convert boolean values to strings 'Yes' or 'No'.
Kata: https://www.codewars.com/kata/53369039d7ab3ac506000467/
*/


#include <stdbool.h>

const char *bool_to_word (bool value)
{
  return (value ? "Yes": "No");
}
