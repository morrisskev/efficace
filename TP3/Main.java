import java.io.File;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Scanner;

class Main {

    public static ArrayList<String> words = new ArrayList<>();
    public static HashMap<String, ArrayList<Integer>> indexes = new HashMap<>();
    public static String text;
    public static HashMap<String, Integer> pointers = new HashMap<>();


    public static void read(String file) throws Exception {
        File f = new File(file);
        Scanner sc = new Scanner(f);
        int counter = Integer.parseInt(sc.nextLine());
        for (int i = 0; i < counter; i++) {
            String line = sc.nextLine();
            String word = "";
            for (int j = 0; j < line.length(); j++) {
                if (line.charAt(j) == '#')
                    break;
                word += line.charAt(j);
            }
            words.add(word);
        }
        while (sc.hasNext()) {
            text += sc.next();
        }
        words.forEach(w -> pointers.put(w, 0));
        sc.close();
    }

    public static void compute(String s, char cur) {
        int index = pointers.get(s);
        if (s.charAt(index) == cur) {
            pointers.put(s, index + 1);
        }
    }

    public static void solve() {
        // char cur;
        // int index = 0;
        // do {
        // cur = text.charAt(index);

        // // Algo ici


        // index++;
        // } while (cur != '#');


        words.forEach(w -> {
            indexes.put(w, new ArrayList<>());
            int index = 0;
            do {
                index = text.indexOf(w, index + 1);
                indexes.get(w).add(index);
            } while (index != -1);
        });

        int max;
        for (int i = 0; i < indexes.size(); i++) {

        }
    }

    public static void main(String[] args) throws Exception {
        read(args[0]);

        solve();
        System.out.println(indexes);
    }
}
