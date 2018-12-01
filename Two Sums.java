package com.company;

import java.util.Scanner;

public class Main {

    // To create an object of Scanner class, we usually pass the predefined object System.in, which represents the standard input stream.
    private static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        // write your code here

        /*Given an array of integers, return indices of the two numbers such that they add up to a specific target.

        You may assume that each input would have exactly one solution, and you may not use the same element twice.

        Example:

        Given nums = [2, 7, 11, 15], target = 9,

        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1].
        */

        //create array and fill it in
        System.out.println("What is the size of the array: ");
        int arraySize = sc.nextInt();

        //array of size arraySize
        int[] inputArray = new int[arraySize];

        for(int i = 0; i < arraySize; i++){
            System.out.println("Enter the integer into the array: ");
            inputArray[i] = sc.nextInt();
        }


        System.out.println("What is the target value: ");
        int compareValue = sc.nextInt();

        //call function
        int[] finalArray = twoSum(inputArray,compareValue);

        //print out return array
        System.out.println(finalArray);


    }

    //method - return type is an int array and parameters are an int array(nums) and variable called target
    public static int[] twoSum(int[] nums, int target){
        //need an array of size 2 to return
        int[] returnArray = new int[2];


        //ok we need to check every two entries to see if the sum equals target
        //let's iterate through the array until the second to last index
        for(int i = 0; i < nums.length-1; i++){

            if((nums[i] + nums[i+1] == target)){
                //if values are the indexes are equal, then input them to the returnArray and return the array
                returnArray[0] = i;
                returnArray[1] = i+1;

                return returnArray;
            }

        }
        //if we get to this point and none of the consecutive entries equal target, then we return an empty array
        return returnArray;
    }

}
