package mergeCSVDatasets.utils;

import com.opencsv.CSVReader;
import com.opencsv.CSVWriter;
import com.opencsv.exceptions.CsvException;
import org.apache.commons.io.filefilter.WildcardFileFilter;

import java.io.*;
import java.util.List;

public class FileUtils {

    public List<String[]> parseCSVFile(String filepath) {
        List<String[]> r;
        try (CSVReader reader = new CSVReader(new FileReader(filepath))) {
            r = reader.readAll();
            return r;
        } catch (IOException | CsvException e) {
            e.printStackTrace();
            return null;
        }
    }

    public void writeFile(String filepath, List<String[]> list, boolean append) {
        try {
            File myObj = new File(filepath);

            if(myObj.createNewFile()) {
                System.out.println("File created.");
            }

            FileWriter fileWriter = new FileWriter(filepath, append);
            CSVWriter csvWriter = new CSVWriter(fileWriter);
            csvWriter.writeAll(list);
            csvWriter.close();
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }

    public File[] getFilesFromFolder(String folderPath, String ext) {
        if(folderPath.equals(""))
            return null;

        if(!folderPath.endsWith("\\"))
            folderPath += "\\";

        folderPath = folderPath.replace("\\", "\\\\").trim();

        File dir = new File(folderPath);
        FileFilter fileFilter = new WildcardFileFilter("*." + ext);
        File[] files = dir.listFiles(fileFilter);

        if(files == null)
            return null;

        if (files.length > 0) {
            return files;
        }
        return null;
    }

    public void addCSVHeader(String filepath, List<String[]> list, List<String[]> headers) {
        writeFile(filepath, headers, false);
        writeFile(filepath, list, true);
    }
}
