/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package matrix;

import java.util.Scanner;

/**
 *
 * @author ADMIN
 */
public class Matrix {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        do{
            //1.Display menu
            displayMenu();
            //2.Get user data
            int choice = getData(1, 4);
            //Perform function based on select option
            switch(choice){
                //Option 1: Addition matrixes
                case 1:
                    displayAddition();
                    //input matrix 1
                    int[][] matrix1 = getMatrix1();
                    //input matrix 2
                    int[][] matrix2 = getMatrix2(matrix1, choice);
                    //add 2 matrix: matrix 1 and matrix 2
                    int[][] result = additionMatrix(matrix1, matrix2);
                    //display result
                    displayResult(matrix1, matrix2, result, choice);
                    break;
                //Option 2: Subtraction matrixes
                case 2:
                    displaySubtraction();
                    //input matrix 1
                    matrix1 = getMatrix1();
                    //input matrix 2
                    matrix2 = getMatrix2(matrix1, choice);
                    //subtraction 2 matrix: matrix 1 to matrix 2
                    result = subtractionMatrix(matrix1, matrix2);
                    //display result
                    displayResult(matrix1, matrix2, result, choice);
                    break;
                //Option 3: Multiplication matrixes
                case 3:
                    displayMultiplication();
                    //input matrix 1
                    matrix1 = getMatrix1();
                    //input matrix 2
                    matrix2 = getMatrix2(matrix1, choice);
                    //multiplication 2 matrix: matrix 1 and matrix 2
                    result = multiplicationMatrix(matrix1, matrix2);
                    //display result
                    displayResult(matrix1, matrix2, result, choice);
                    break;
                //Option 4: Exit program
                case 4:
                    System.exit(0);
                    break;
            }
        }while(true);

    }

    
    
    public static void displayMenu(){
        System.out.println("====Calculate matrix====");
        System.out.println("1. Add");
        System.out.println("2. Sub");
        System.out.println("3. Mul");
        System.out.println("4. Exit");
        System.out.print("Your choice: ");
    }
    


    public static int[][] getMatrix1() {
        int col, row;
        System.out.print("Enter Row Matrix 1:");
        row = getData(0, Integer.MAX_VALUE);
        System.out.print("Enter Column Matrix 1:");
        col = getData(0, Integer.MAX_VALUE);
        int[][] matrix1 = new int[row][col];
        //traverse from first row to the last row of matrix
        for(int i=0; i<row; i++){
            //traverse from first element to last element of row of matrx
            for(int j=0; j<col; j++){
                String msg= String.format("Enter Matrix1[%d][%d]:", (i+1), (j+1));
                matrix1[i][j] = getMatrix(msg);
            }
        }
        return matrix1;
    }
    
    public static int getData(int min, int max){
        Scanner sc = new Scanner(System.in);
        int data;
        do{
            try{
                //Check input is the integer number
                data = Integer.parseInt(sc.nextLine());
                //Check out of range
                if (data <min || data >max){
                    System.out.println("Please enter positive decimal number from "+min+" to "+max);
                } else break;
            } catch (NumberFormatException exception){
                System.out.println("Please enter positive decimal number.");
            }
        } while (true);
        return data;
    }

    public static int[][] getMatrix2(int[][] matrix1, int choice) {
        int row1 = matrix1.length;
        int col1 = matrix1[0].length;
        System.out.print("Enter Row Matrix 2:");
        int row2 = getData(0, Integer.MAX_VALUE);
        System.out.print("Enter Column Matrix 2:");
        int col2 = getData(0, Integer.MAX_VALUE);
        do{
            //Add and sub, number row and column of matrix 1 and 2 are need equal
            if ((choice == 1 || choice ==2)&&((row1!=row2)||(col1!=col2))){
                System.out.println("Number row and column of matrix 1 and 2 are not equal.");
                System.out.print("Enter Row Matrix 2:");
                row2 = getData(0, Integer.MAX_VALUE);
                System.out.print("Enter Column Matrix 2:");
                col2 = getData(0, Integer.MAX_VALUE);
            } 
            //In mul, compare number column of matrix1 and number row of matrix2
            else if (choice == 3 && col1 != row2){
                System.out.println("Number column of matrix1 and number row of matrix2 are not equal.");
                System.out.print("Enter Row Matrix 2:");
                row2 = getData(0, Integer.MAX_VALUE);
            } else break;          
        } while(true);

        int[][] matrix2 = new int[row2][col2];
        //traverse from first row to the last row of matrix
        for (int i =0; i<row2; i++){
            //traverse from first element to last element of row of matrx
            for (int j = 0; j<col2; j++){
                String msg= String.format("Enter Matrix2[%d][%d]:", (i+1), (j+1));
                matrix2[i][j] = getMatrix(msg);
            }
        }
        return matrix2;
    }

    public static void displayAddition() {
        System.out.println("-----Addition-----");
    }

    public static int[][] additionMatrix(int[][] matrix1, int[][] matrix2) {
        int row = matrix1.length;
        int col = matrix1[0].length;
        int[][] result = new int[row][col];
        //traverse from first element of row to last element of row of matrix
        for (int i = 0; i < row; i++) {
            //traverse from first element of column to last element of column of matrix
            for (int j = 0; j < col; j++) {
                result[i][j]= matrix1[i][j] + matrix2[i][j];
            }
        }
        return result;
    }

    public static void displayResult(int[][] matrix1, int[][] matrix2, int[][] result, int choice) {
        System.out.println("-----Result-----");
        displayMatrix(matrix1);
        if (choice == 1){
            System.out.println("+");
        } else if (choice == 2){
            System.out.println("-");
        } else System.out.println("*");
        displayMatrix(matrix2);
        System.out.println("=");
        displayMatrix(result);
    }

    public static void displaySubtraction() {
        System.out.println("-----Substraction-----");
    }

    public static void displayMultiplication() {
        System.out.println("-----Multiplication-----");
    }

    public static int[][] subtractionMatrix(int[][] matrix1, int[][] matrix2) {
        int row = matrix1.length;
        int col = matrix1[0].length;
        int[][] result = new int[row][col];
        //traverse from first element of row to last element of row of matrix
        for (int i = 0; i < row; i++) {
            //traverse from first element of column to last element of column of matrix
            for (int j = 0; j < col; j++) {
                result[i][j]= matrix1[i][j] - matrix2[i][j];
            }
        }
        return result;
    }

    public static int[][] multiplicationMatrix(int[][] matrix1, int[][] matrix2) {
        int rowM1 = matrix1.length;
        int rowM2 = matrix2.length;
        int colM2 = matrix2[0].length;
        int[][] result = new int[rowM1][colM2];
        //traverse from first element of row to last element of row of matrix 1
        for (int i = 0; i < rowM1; i++) {
            //traverse from first element of column to last element of column of matrix 2
            for (int j = 0; j < colM2; j++) {
                //traverse from first element of row to last element of row of matrix 1
                for (int k = 0; k < rowM2; k++) {
                    result[i][j] += matrix2[k][j] * matrix1[i][k];
                }
            }
        }
        return result;
    }
    public static void displayMatrix(int[][] matrix) {
        int row = matrix.length;
        int col = matrix[0].length;
        //traverse from first element of row to last element of row of matrix
        for (int i = 0; i < row; i++) {
            //traverse from first element of column to last element of column of matrix
            for (int j = 0; j < col; j++) {
                System.out.format("[%d]", matrix[i][j]);
            }
            System.out.println();
        }
    }
    
    public static int getMatrix(String msg){
        Scanner sc = new Scanner(System.in);
        int data;
        do{
            try{
                System.out.print(msg);
                data = Integer.parseInt(sc.nextLine());
                break;
            } catch (NumberFormatException exception){
                System.out.println("Value of matrix is digit");
            }
        } while (true);
        return data;
    }
}
