import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Map;
import java.util.Scanner;
import java.util.AbstractMap.SimpleEntry;

public class Main {

    static int nbCities;
    static int nbTypeA, nbTypeB, nbTypeC;
    // Tous les chemins possibles
    static HashMap<String, ArrayList<String>> cityPaths = new HashMap<>();
    // Les crédits de départ pour chaque ville, get(0) = Type A, get(2) = Type C
    static HashMap<String, ArrayList<Integer>> cityCredits = new HashMap<>();
    // La distance entre deux villes
    static HashMap<SimpleEntry<String, String>, Integer> cityDistance = new HashMap<>();
    // Villes déjà visitées
    static HashSet<String> visited = new HashSet<>();
    // Résultat final
    static ArrayList<ArrayList<String>> resultA = new ArrayList<>();
    static ArrayList<ArrayList<String>> resultB = new ArrayList<>();
    static ArrayList<ArrayList<String>> resultC = new ArrayList<>();
    // Fichier out
    static String outFileName;

    public static void parse(String file) throws FileNotFoundException {
        outFileName = file.replaceAll(".in", ".out");
        File input = new File(file);
        Scanner sc = new Scanner(input);
        nbCities = Integer.parseInt(sc.nextLine());
        nbTypeA = Integer.parseInt(sc.nextLine());
        nbTypeB = Integer.parseInt(sc.nextLine());
        nbTypeC = Integer.parseInt(sc.nextLine());

        for (int i = 0; i < nbCities; i++) {
            String line = sc.nextLine();
            String[] words = line.split(" ");
            String city = words[0];
            int creditA = Integer.parseInt(words[1]);
            int creditB = Integer.parseInt(words[2]);
            int creditC = Integer.parseInt(words[3]);
            ArrayList<Integer> credits = new ArrayList<>();
            credits.add(creditA);
            credits.add(creditB);
            credits.add(creditC);

            cityCredits.put(city, credits);
        }

        while (sc.hasNextLine()) {
            String line = sc.nextLine();
            String[] words = line.split(" ");
            String fCity = words[0];
            String sCity = words[1];
            Integer dist = Integer.parseInt(words[2]);

            // Reciproque
            if (cityPaths.get(fCity) != null) {
                cityPaths.get(fCity).add(sCity);
            } else {
                ArrayList<String> temp = new ArrayList<>();
                temp.add(sCity);
                cityPaths.put(fCity, temp);
            }

            if (cityPaths.get(sCity) != null) {
                cityPaths.get(sCity).add(fCity);
            } else {
                ArrayList<String> temp = new ArrayList<>();
                temp.add(fCity);
                cityPaths.put(sCity, temp);
            }

            // Reciproque
            SimpleEntry<String, String> e1 = new SimpleEntry<>(fCity, sCity);
            SimpleEntry<String, String> e2 = new SimpleEntry<>(sCity, fCity);
            cityDistance.put(e1, dist);
            cityDistance.put(e2, dist);

        }

        sc.close();
    }

    public static String bestStart(int busType) {
        var maxWrapper = new Object() {
            int ordinal = 0;
            String key = "";
        };
        cityCredits.forEach((k, v) -> {
            if (!visited.contains(k)) {
                int cur = cityCredits.get(k).get(busType);
                if (cur > maxWrapper.ordinal) {
                    maxWrapper.ordinal = cur;
                    maxWrapper.key = k;
                }
            }
        });
        return maxWrapper.key;
    }

    public static boolean busRemains(int busType) {
        switch (busType) {
            case 0:
                return nbTypeA > 0;
            case 1:
                return nbTypeB > 0;
            case 2:
                return nbTypeC > 0;
            default:
                return false;
        }
    }

    public static SimpleEntry<String, Integer> trueBestStart() {
        String bestCity = "";
        Integer index = -1;
        Integer max = 0;
        Iterator<Map.Entry<String, ArrayList<Integer>>> it = cityCredits.entrySet().iterator();
        while (it.hasNext()) {
            Map.Entry<String, ArrayList<Integer>> pair = it.next();
            for (int i = 0; i < 3; i++) {
                Integer cur = pair.getValue().get(i);
                // System.out.println("Cur is : " + cur + ", max is : " + max);
                if (cur > max && busRemains(i) && !visited.contains(pair.getKey())) {
                    max = cur;
                    index = i;
                    bestCity = pair.getKey();
                }
            }
        }
        SimpleEntry<String, Integer> result = new SimpleEntry<>(bestCity, index);
        return result;

    }

    public static int distance(String from, String to) {
        SimpleEntry<String, String> path = new SimpleEntry<>(from, to);
        return cityDistance.get(path);
    }

    public static String bestPath(String start, int credits) {
        ArrayList<String> possiblePaths = cityPaths.get(start);
        var minWrapper = new Object() {
            int ordinal = 100000;
            String key = "";
        };
        possiblePaths.forEach((next) -> {
            if (!visited.contains(next)) {
                int cur = distance(start, next);
                if (cur < minWrapper.ordinal && credits >= cur) {
                    minWrapper.ordinal = cur;
                    minWrapper.key = next;
                }
            }
        });
        return minWrapper.key;
    }

    public static void shortestPath() {
        // while (nbTypeA != 0) {
        // ArrayList<String> pathA = new ArrayList<>();
        // String start = bestStart(0);
        // if (start == "")
        // break;
        // pathA.add(start);
        // visited.add(start);
        // int credits = cityCredits.get(start).get(0);
        // String cur = start;
        // while (credits > 0) {
        // String nextPath = bestPath(cur, credits);
        // if (nextPath == "")
        // break;
        // credits -= distance(cur, nextPath);
        // pathA.add(nextPath);
        // visited.add(nextPath);
        // cur = nextPath;
        // }
        // resultA.add(pathA);
        // nbTypeA--;
        // }
        // while (nbTypeB != 0) {
        // ArrayList<String> pathB = new ArrayList<>();
        // String start = bestStart(1);
        // if (start == "")
        // break;
        // pathB.add(start);
        // visited.add(start);
        // int credits = cityCredits.get(start).get(1);
        // String cur = start;
        // while (credits > 0) {
        // String nextPath = bestPath(cur, credits);
        // if (nextPath == "")
        // break;
        // credits -= distance(cur, nextPath);
        // pathB.add(nextPath);
        // visited.add(nextPath);
        // cur = nextPath;
        // }
        // resultB.add(pathB);
        // nbTypeB--;
        // }
        // while (nbTypeC != 0) {
        // ArrayList<String> pathC = new ArrayList<>();
        // String start = bestStart(2);
        // if (start == "")
        // break;
        // pathC.add(start);
        // visited.add(start);
        // int credits = cityCredits.get(start).get(2);
        // String cur = start;
        // while (credits > 0) {
        // String nextPath = bestPath(cur, credits);
        // if (nextPath == "")
        // break;
        // credits -= distance(cur, nextPath);
        // pathC.add(nextPath);
        // visited.add(nextPath);
        // cur = nextPath;
        // }
        // resultC.add(pathC);
        // nbTypeC--;
        // }
        while (nbTypeA + nbTypeB + nbTypeC != 0) {
            SimpleEntry<String, Integer> bestStart = trueBestStart();
            String start = bestStart.getKey();
            int type = bestStart.getValue();
            // System.out.println("Starting city " + start + ", type = " + type);
            if (type == 0) {
                ArrayList<String> pathA = new ArrayList<>();
                pathA.add(start);
                visited.add(start);
                int credits = cityCredits.get(start).get(0);
                String cur = start;
                while (credits > 0) {
                    String nextPath = bestPath(cur, credits);
                    if (nextPath == "")
                        break;
                    credits -= distance(cur, nextPath);
                    pathA.add(nextPath);
                    visited.add(nextPath);
                    cur = nextPath;
                }
                resultA.add(pathA);
                nbTypeA--;
            }

            else if (type == 1) {

                ArrayList<String> pathB = new ArrayList<>();
                pathB.add(start);
                visited.add(start);
                int credits = cityCredits.get(start).get(1);
                String cur = start;
                while (credits > 0) {
                    String nextPath = bestPath(cur, credits);
                    if (nextPath == "")
                        break;
                    credits -= distance(cur, nextPath);
                    pathB.add(nextPath);
                    visited.add(nextPath);
                    cur = nextPath;
                }
                resultB.add(pathB);
                nbTypeB--;
            }

            else if (type == 2) {
                ArrayList<String> pathC = new ArrayList<>();
                pathC.add(start);
                visited.add(start);
                int credits = cityCredits.get(start).get(2);
                String cur = start;
                while (credits > 0) {
                    String nextPath = bestPath(cur, credits);
                    if (nextPath == "")
                        break;
                    credits -= distance(cur, nextPath);
                    pathC.add(nextPath);
                    visited.add(nextPath);
                    cur = nextPath;
                }
                resultC.add(pathC);
                nbTypeC--;
            }

            else {
                break;
            }
        }

    }

    public static void output() throws Exception {
        PrintWriter writer = new PrintWriter(outFileName);
        int compt = 0;
        while ( compt < resultA.size() || compt < resultB.size() || compt < resultC.size() ){
            if (compt < resultA.size()) {
                writer.println("###");
                writer.println("A");
                for (String city : resultA.get(compt)){
                    writer.println(city);
                }
            }
            if (compt < resultB.size()) {
                writer.println("###");
                writer.println("B");
                for (String city : resultB.get(compt)){
                    writer.println(city);
                }
            }
            if (compt < resultC.size()) {
                writer.println("###");
                writer.println("C");
                for (String city : resultC.get(compt)){
                    writer.println(city);
                }
            }
            compt ++;
        }  
        writer.close();
    }

    public static void main(String[] args) throws Exception {


        parse(args[0]);

        // // Crédits initiaux :
        // cityCredits.forEach((k, v) -> {
        // System.out.println("Ville : " + k);
        // System.out.println("Credits Bus A : " + v.get(0));
        // System.out.println("Credits Bus B : " + v.get(1));
        // System.out.println("Credits Bus C : " + v.get(2));

        // });

        // // Villes liées :
        // cityPaths.forEach((k, v) -> {
        // System.out.println("La ville " + k + " est connectée à " + v);
        // });

        // // Distances :
        // cityDistance.forEach((k, v) -> {
        // System.out.println("Paire de villes : " + k);
        // System.out.println("Distance : " + v);
        // });

        shortestPath();

        output();

    }
}
