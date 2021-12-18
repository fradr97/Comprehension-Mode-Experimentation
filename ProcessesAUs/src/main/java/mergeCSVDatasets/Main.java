package mergeCSVDatasets;

import mergeCSVDatasets.merge.OpenFaceDataset;
import mergeCSVDatasets.utils.FileUtils;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        FileUtils fileUtils = new FileUtils();

        /** Script used to process the OpenFace output dataset (taking only the AUs)
         *  and add the timestamp starting from the file creation date
         *  6 is the number of tasks (and then folders) */
        int tasksNumber = 6;
        for(int i = 0; i < tasksNumber; i ++) {
            int folderIndex = i + 1;
            String openFaceDatasetsFolderPath = "C:\\Users\\Francesco\\Desktop\\Sperimentazione\\9. Jonathan\\task" + folderIndex + "\\OpenFace\\";
            String targetFolderPath = openFaceDatasetsFolderPath + "openFace.csv";
            OpenFaceDataset openFaceDataset = new OpenFaceDataset(openFaceDatasetsFolderPath, targetFolderPath);
            List<String[]> openFaceList = fileUtils.parseCSVFile(openFaceDataset.getOutputFile().toString());
        }
    }

    private static void addHeader(String filePath, List<String[]> list) {
        FileUtils fileUtils = new FileUtils();

        String[] header = new String[] {
                "Time", "LE", "F4", "C4", "P4", "P3", "C3", "F3", "Trigger",
                "Time_Offset", "ADC_Status", "ADC_Sequence", "Event", "Comments"
        };

        List<String[]> headerList = new ArrayList<>();
        headerList.add(header);

        fileUtils.addCSVHeader(filePath, list, headerList);
    }
}
