package openFaceOutput;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class ProcessOpenFaceOutput {
    public static final int OF_TIMESTAMP = 2;

    public static final int OF_AU01_r = 679;
    public static final int OF_AU02_r = 680;
    public static final int OF_AU04_r = 681;
    public static final int OF_AU05_r = 682;
    public static final int OF_AU06_r = 683;
    public static final int OF_AU07_r = 684;
    public static final int OF_AU09_r = 685;
    public static final int OF_AU10_r = 686;
    public static final int OF_AU12_r = 687;
    public static final int OF_AU14_r = 688;
    public static final int OF_AU15_r = 689;
    public static final int OF_AU17_r = 690;
    public static final int OF_AU20_r = 691;
    public static final int OF_AU23_r = 692;
    public static final int OF_AU25_r = 693;
    public static final int OF_AU26_r = 694;
    public static final int OF_AU45_r = 695;

    private static final String OPEN_FACE_DATASET_DIRECTORY_COMPLETE = "C:\\Users\\Francesco\\Desktop\\output\\complete.csv";

    private final File file;
    private final FileUtils fileUtils;

    public ProcessOpenFaceOutput(String outputFolderPath) {
        this.fileUtils = new FileUtils();
        this.mergeOpenFaceOutputs(outputFolderPath);

        File fileTemp = new File(OPEN_FACE_DATASET_DIRECTORY_COMPLETE);

        if(!fileTemp.exists())
            fileTemp = defaultOpenFaceOutput();

        this.file = fileTemp;
    }

    private File defaultOpenFaceOutput() {
        return new File("C:\\Users\\Francesco\\Desktop\\output\\webcam_2021-11-01-10-25.csv");
    }

    //TODO: pass openFaceOutput as parameter
    public void mergeOpenFaceOutputs(String outputFolderPath) {
        File[] files;
        files = fileUtils.getFilesFromFolder(outputFolderPath, "csv");

        if (files != null) {
            List<String[]> newOpenFaceList = new ArrayList<>();
            String[] newLine;

            String[] headers = new String[] {
                    "Timestamp", "AU01", "AU02", "AU04", "AU05", "AU06", "AU07", "AU09",
                    "AU10", "AU12", "AU14", "AU15", "AU17", "AU20", "AU23", "AU25", "AU26", "AU45"
            };
            newOpenFaceList.add(headers);

            for (File openFaceFile : files) {
                List<String[]> list = this.fileUtils.parseCSVFile(openFaceFile.toString()); // as MutableList<Array<String>>

                for(int i = 1; i < list.size(); i ++) {  //position 0 is the header
                    newLine = getNewOFLine(openFaceFile, list, i);
                    newOpenFaceList.add(newLine);
                }
            }
            //TODO: remove filePath
            fileUtils.writeFile(OPEN_FACE_DATASET_DIRECTORY_COMPLETE, newOpenFaceList, false);
        }
    }

    private String[] getNewOFLine(File file, List<String[]> list, int index) {
        DateTimeUtils dateTimeUtils = new DateTimeUtils();
        String dateTime = dateTimeUtils.dataCreationAddedToTimeLaps(file, list.get(index)[OF_TIMESTAMP]);

        return new String[]{dateTime,
                list.get(index)[OF_AU01_r],
                list.get(index)[OF_AU02_r],
                list.get(index)[OF_AU04_r],
                list.get(index)[OF_AU05_r],
                list.get(index)[OF_AU06_r],
                list.get(index)[OF_AU07_r],
                list.get(index)[OF_AU09_r],
                list.get(index)[OF_AU10_r],
                list.get(index)[OF_AU12_r],
                list.get(index)[OF_AU14_r],
                list.get(index)[OF_AU15_r],
                list.get(index)[OF_AU17_r],
                list.get(index)[OF_AU20_r],
                list.get(index)[OF_AU23_r],
                list.get(index)[OF_AU25_r],
                list.get(index)[OF_AU26_r],
                list.get(index)[OF_AU45_r]
        };
    }

    public List<String[]> getOpenFaceAUs() {
        List<String[]> newOpenFaceList = new ArrayList<>();
        String[] newLine;
        List<String[]> openFaceOutput = this.fileUtils.parseCSVFile(this.file.toString());

        for (int i = 1; i < openFaceOutput.size(); i ++) {  //position 0 is the header
            newLine = getNewOFLine(file, openFaceOutput, i);
            newOpenFaceList.add(newLine);
        }
        return newOpenFaceList;
    }
}