import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.io.FileReader;
import java.util.List;
import java.util.Random;


public class Hangman {

    private static String currentWord;
    private static ArrayList<String> words;
    private static ArrayList<Character> userGuesses;

    private static List<String> loadWords() throws IOException {
        List<String> wordsLocal = new ArrayList<String>();
        BufferedReader br = new BufferedReader(new FileReader("words.txt"));
        String line;
        while ((line = br.readLine()) != null) {
            wordsLocal.add(line);
        }
        return wordsLocal;
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

    public static void main(String[] args) throws IOException {
        words = (ArrayList<String>) loadWords();
        currentWord = words.get(selectRandomElement());
        System.out.println(printWordString());
    }
}
