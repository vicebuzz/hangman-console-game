import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.io.FileReader;
import java.util.List;
import java.util.Random;
import java.util.Scanner;


public class Hangman {

    private static String currentWord;
    private static ArrayList<String> words;
    private static ArrayList<Character> userGuesses = new ArrayList<Character>();
    private static Boolean gameOver = false;
    private static Integer wordCount = 0;
    private static Integer tries = 6;

    private static List<String> loadWords() throws IOException {
        List<String> wordsLocal = new ArrayList<String>();
        BufferedReader br = new BufferedReader(new FileReader("words.txt"));
        String line;
        while ((line = br.readLine()) != null) {
            wordsLocal.add(line);
        }
        return wordsLocal;
    }

    private static List<String> loadArt() {
        List<String> artLocal = new ArrayList<String>();
        try {
            BufferedReader br = new BufferedReader(new FileReader("words.txt"));
            String line;
            while ((line = br.readLine()) != null) {
                artLocal.add(line);
            }
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        return artLocal;
    }

    public static Integer selectRandomElement() {
        Random rand = new Random();
        int randomIndex = rand.nextInt(words.size());
        return randomIndex;
    }

    public static String printWordString(){
        String dashes = "";
        if (userGuesses != null){
            for (int i = 0; i < currentWord.length(); i++){
                if(userGuesses.contains(currentWord.charAt(i))){
                    dashes += currentWord.charAt(i);
                    dashes += " ";
                } else{
                    dashes += "_ ";
                }
            }
        } else {
            for (int i = 0; i < currentWord.length(); i++){
                dashes += "_ ";
            }
        }
        return dashes;
    }

    public static Boolean checkIfUserGuessed(){
        int count = 0;
        for (Character c:currentWord.toCharArray()){
            if (userGuesses.contains(c)){
                count++;
            }
        }
        if (count == currentWord.length()){
            return true;
        }
        return false;
    }

    public static Boolean askUserToContinueTheGame(){
        Scanner scannerLocal = new Scanner(System.in);
        System.out.println("Well done, this is the word, now do you want to continue?");
        String userChoice = scannerLocal.nextLine();
        Boolean returnChoice = null;
        if (userChoice.equals("y")){
            returnChoice = true;
        } else if (userChoice.equals("n")) {
            returnChoice = false;
        } else {
            System.out.println("invalid input");
            askUserToContinueTheGame();
        }
        return returnChoice;
    }

    public static void main(String[] args) throws IOException {
        words = (ArrayList<String>) loadWords();
        Scanner myObj = new Scanner(System.in);
        currentWord = words.get(selectRandomElement());
        System.out.println(currentWord);
        while (!gameOver){

            System.out.println(printWordString());
            String userInput = myObj.nextLine();

            if (userInput.length() == 1){
                if (currentWord.contains(userInput)){
                    userGuesses.add(userInput.toCharArray()[0]);
                } else{
                    tries -= 1;
                }
            } else if (userInput.length() > 1){
                if (userInput.equals(currentWord)){
                    System.out.println(printWordString());
                    wordCount++;
                    Boolean choice = askUserToContinueTheGame();
                    if (choice){
                        main(null);
                    } else if (!choice) {
                        System.out.println("Sorry to see you go, so far you guessed " + wordCount + " words total");
                    }
                    gameOver = true;
                } else {
                    tries -= 1;
                    System.out.println("This is not the word");
                }
            } else {
                System.out.println("Invalid input!");
            }
            if (tries == 0){
                System.out.println("You failed to guess " + currentWord + ", but you guessed " + wordCount + " other words");
                gameOver = true;
            } else {
                if (checkIfUserGuessed()){
                    System.out.println(printWordString());
                    wordCount++;
                    Boolean choice = askUserToContinueTheGame();
                    if (choice){
                        main(null);
                    } else if (!choice) {
                        System.out.println("Sorry to see you go, so far you guessed " + wordCount + " words total");
                    }
                    gameOver = true;
                } else{
                    continue;
                }
            }
        }
    }
}
