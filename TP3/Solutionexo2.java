import java.util.*;
import java.io.File;
import java.io.FileNotFoundException;
import java.lang.StringBuilder;
import java.util.HashMap;

public class Solutionexo2 {
  public static ArrayList<String>getWords(String file) throws FileNotFoundException{
    //Prend toutes les chaines s1,..,sn du fichier
    ArrayList<String>words=new ArrayList<String>();
    File input=new File(file);
    Scanner sc=new Scanner(input);
    String getnum=sc.nextLine();
    int num=Integer.parseInt(getnum);
    for(int i=0;i<num;i++){
      String s=sc.nextLine();
      words.add(String.valueOf(s.subSequence(0,s.length()-1)));
    }
    return words;
  }

  public static HashMap<String,String>getReverses(ArrayList<String>words){
    //Calcule pour chaque chaine si son inverse
    HashMap<String,String>reverse=new HashMap<String,String>();
    for(String s:words){
      StringBuilder sb=new StringBuilder(s);
      sb.reverse();
      reverse.put(s,sb.toString());
    }
    return reverse;
  }

  public static boolean isIn(String s,ArrayList<String>list){
    for(String s2 : list){
      if(s.equals(s2)){
        return true;
      }
    }
    return false;
  }
  public static void main(String[] args)throws FileNotFoundException{
    ArrayList<String> words=null;
    words=getWords("request.txt");
    HashMap<String,String> dic=getReverses(words);
    ArrayList<String> toDelete=new ArrayList<>();
    String chaine="";
    for(String s : words){
      if(!isIn(s,toDelete)){
        chaine+=s;
        toDelete.add(s);
        toDelete.add(dic.get(s));
      }
    }
    System.out.println(chaine);
  }
}
//Fait par Rayane AMAURY
