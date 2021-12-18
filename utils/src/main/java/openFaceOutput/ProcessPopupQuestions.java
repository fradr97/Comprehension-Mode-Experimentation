package openFaceOutput;

import org.json.JSONArray;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.Random;

public class ProcessPopupQuestions {
    private JSONArray tasks;
    private JSONArray taskQuestions;
    private JSONArray questions;
    private String question;
    private String[] answers;
    private ArrayList<Integer> alreadyAsked;

    public ProcessPopupQuestions() {
        //this.answers = new ArrayList<>();
        this.alreadyAsked = new ArrayList<>();
    }

    public String getQuestion() {
        return this.question;
    }

    public String[] getAnswers() {
        return this.answers;
    }

    public boolean checkQuestionExists(String filePath, String javaClass, int line) {
        int taskIndex = this.getTaskIndex(filePath, javaClass);

        if(taskIndex != -1) {
            int taskQuestionIndex = this.getTaskQuestionIndex(taskIndex, line);

            if(taskQuestionIndex != -1) {
                int questionAnswersIndex = this.getQuestionAnswersIndex(taskQuestionIndex);

                if(questionAnswersIndex != -1) {
                    this.updateAlreadyAskedQuestions(questionAnswersIndex);

                    this.question = questions.getJSONObject(questionAnswersIndex).getString("question");
                    JSONArray ans = questions.getJSONObject(questionAnswersIndex).getJSONArray("answers");

                    this.answers = new String[ans.length()];
                    for(int k = 0; k < ans.length(); k ++) {
                        this.answers[k] = ans.get(k).toString();
                        //this.answers.add(answers.get(k).toString());
                    }
                    return true;
                }
                return false;
            }
            return false;
        }
        return false;
    }

    private int getTaskIndex(String filePath, String javaClass) {
        FileUtils fileUtils = new FileUtils();
        String content = fileUtils.readFileContent(filePath);

        try {
            JSONObject jsonContent = new JSONObject(content);
            this.tasks = jsonContent.getJSONArray("tasks");

            for (int i = 0; i < this.tasks.length(); i ++){
                String task = this.tasks.getJSONObject(i).getString("task");
                if(javaClass.contains(task)) {
                    return i;
                }
            }
        } catch (Exception e) {
            return -1;
        }
        return -1;
    }

    private int getTaskQuestionIndex(int taskIndex, int line) {
        try {
            this.taskQuestions = this.tasks.getJSONObject(taskIndex).getJSONArray("taskQuestions");
            for (int j = 0; j < this.taskQuestions.length(); j++) {
                int from = this.taskQuestions.getJSONObject(j).getInt("fromLine");
                int to = this.taskQuestions.getJSONObject(j).getInt("toLine");
                boolean isInRange = numIsInRange(line, from, to);
                if(isInRange) {
                    return j;
                }
            }
        } catch (Exception e) {
            return -1;
        }
        return -1;
    }

    private int getQuestionAnswersIndex(int taskQuestionIndex) {
        try {
            this.questions = this.taskQuestions.getJSONObject(taskQuestionIndex).getJSONArray("questions");
            Random r = new Random();
            int rIndex = r.nextInt(this.questions.length());

            /* if all the questions have already been asked,
             clear the index array and propose them again */
            if(questions.length() == this.alreadyAsked.size()) {
                this.alreadyAsked.clear();
            } else {
                while(isAlreadyAsked(rIndex)) {
                    rIndex = r.nextInt(questions.length());
                }
            }
            return rIndex;
        } catch (Exception ex) {
            return -1;
        }
    }

    private boolean isAlreadyAsked(int index) {
        for (int i : this.alreadyAsked) {
            if (i == index)
                return true;
        }
        return false;
    }

    private void updateAlreadyAskedQuestions(int index) {
        this.alreadyAsked.add(index);
    }

    private boolean numIsInRange(int num, int from, int to) {
        return num >= from && num <= to;
    }
}
