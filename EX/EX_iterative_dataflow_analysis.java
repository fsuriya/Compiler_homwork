import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files

class IDA{
    public static void main(String[] args) {
        try{
            File myFile = new File("state.txt");
            Scanner Input = new Scanner(myFile);
            while(Input.hasNextLine()){
                String data = Input.nextLine();
                System.out.println(data);
            }
        } catch (FileNotFoundException e){
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }
}