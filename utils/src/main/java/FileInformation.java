import openFaceOutput.ProcessPopupQuestions;

import javax.swing.*;
import java.util.*;

public class FileInformation {
    public static final int TIMESTAMP = 0;

    public static final int AU01_r = 1;
    public static final int AU02_r = 2;
    public static final int AU04_r = 3;
    public static final int AU05_r = 4;
    public static final int AU06_r = 5;
    public static final int AU07_r = 6;
    public static final int AU09_r = 7;
    public static final int AU10_r = 8;
    public static final int AU12_r = 9;
    public static final int AU14_r = 10;
    public static final int AU15_r = 11;
    public static final int AU17_r = 12;
    public static final int AU20_r = 13;
    public static final int AU23_r = 14;
    public static final int AU25_r = 15;
    public static final int AU26_r = 16;
    public static final int AU45_r = 17;

    HashMap<Integer, Integer> map = new HashMap<>();

    public static void main(String[] args) {
        //String filePath = "C:\\Users\\Francesco\\Desktop\\final-coding-mode-events.csv";
    }

    private static boolean isAttentionDropped(ArrayList<Integer> buffer) {
        int val = buffer.get(0);

        for(int i = 1; i < buffer.size(); i ++) {
            if(buffer.get(i) <= val)
                val = buffer.get(i);
            else return false;
        }

        int firstValue = buffer.get(0);
        int lastValue = buffer.get(buffer.size() - 1);
        int diff = firstValue - lastValue;
        return diff <= 10;
    }

    private static int getLastAttentionValue(List<String[]> list, int line) {
        for(int i = list.size() - 1; i > 0; i --) {
            if(Integer.parseInt(list.get(i)[4]) == line)
                return Integer.parseInt(list.get(i)[8]);
        }
        return -1;
    }

    private static int countLineOccurrence(List<String[]> list, int line) {
        int count = 0;
        
        for(int i = 1; i < list.size(); i ++) {
            if(Integer.parseInt(list.get(i)[4]) == line) {
                count ++;
            }
        }
        return count;
    }

    private static void getQuestion() {
        String filePath = "C:\\Users\\Francesco\\Desktop\\questions\\questions.json";
        ProcessPopupQuestions popupQuestions = new ProcessPopupQuestions();

        String javaClass = "Solution1"; //lo ottengo vedendo il file su cui ho il focus

        boolean check = popupQuestions.checkQuestionExists(filePath, "Solution2", 2);
        if(check) {
            String question = popupQuestions.getQuestion();
            String[] answers = popupQuestions.getAnswers();

            JList list = new JList(answers);
            JOptionPane.showMessageDialog(
                    null, list, question, JOptionPane.PLAIN_MESSAGE);
            System.out.println(list.getSelectedValue());
        }
        else System.out.println("No domanda!");
    }

    private static String replaceLastOccurrence(String string, String oldOcc, String newOcc) {
        int i = string.length() - 1;

        if(string.contains(oldOcc)) {
            while (i > 0 && !String.valueOf(string.charAt(i)).equals(oldOcc)) {
                i --;
            }
            return string.substring(0, i) + newOcc + string.substring(i + 1);
        }
        return string;
    }
}