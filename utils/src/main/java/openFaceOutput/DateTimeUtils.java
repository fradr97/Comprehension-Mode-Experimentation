package openFaceOutput;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.attribute.BasicFileAttributes;
import java.nio.file.attribute.FileTime;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.TimeZone;

public class DateTimeUtils {
    private SimpleDateFormat sdf;

    public String dataCreationAddedToTimeLaps(File file, String timeLapse) {
        String dataCreationDateTime = getDataCreationFile(file);
        String date = dataCreationDateTime.substring(0, 10);
        String time = dataCreationDateTime.substring(11);
        timeLapse = timeLapseToTime(timeLapse);

        return date + " " + sumTimes(time, timeLapse);
    }

    public Date getDateFromString(String dateTime) {
        SimpleDateFormat formatter = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSS");
        Date date;

        try {
            date = formatter.parse(dateTime);
        } catch (ParseException e) {
            return getDateFromString("1900-01-01 00:00:00.000");
        }
        return date;
    }

    public String getDataCreationFile(File file) {
        BasicFileAttributes attrs;
        try {
            attrs = Files.readAttributes(file.toPath(), BasicFileAttributes.class);
            FileTime time = attrs.creationTime();

            String pattern = "yyyy-MM-dd HH:mm:ss:SSS";
            SimpleDateFormat simpleDateFormat = new SimpleDateFormat(pattern);

            return simpleDateFormat.format(new Date(time.toMillis()));
        } catch (IOException e) {
            return "0000-00-00 00:00:00:000";
        }
    }

    public String sumTimes(String time1, String time2) {
        this.sdf = new SimpleDateFormat("HH:mm:ss:SSS");
        this.sdf.setTimeZone(TimeZone.getTimeZone("UTC"));

        long sum;
        Date date1;
        Date date2;
        try {
            date1 = this.sdf.parse(time1);
            date2 = this.sdf.parse(time2);
            sum = date1.getTime() + date2.getTime();
        } catch (ParseException e) {
            return null;
        }
        return this.sdf.format(new Date(sum));
    }

    public String timeLapseToTime(String timeLapse) {
        timeLapse = timeLapse.trim().replace(".", ":");
        int occ = countOccurrence(timeLapse, ":");

        if(occ == 1) {  //sec, mill
            timeLapse = "00:00:" + timeLapse;
        }
        else if (occ == 2) {    //min, sec, mill
            timeLapse = "00:" + timeLapse;
        }
        return timeLapse;
    }

    private int countOccurrence(String string, String type) {
        int occ = 0;

        for(int i = 0; i < string.length(); i ++) {
            if((string.charAt(i) + "").equals(type)) {
                occ ++;
            }
        }
        return occ;
    }

    public Boolean checkSameDates(Date date1, Date date2) {
        return datesMilliesDiff(date1, date2) <= 1000;
    }

    /*public Long datesMilliesDiff(String pluginDate, String ofDate) {
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSS");
        //sdf = TimeZone.getTimeZone("UTC")

        Long diff;
        Date dt1;
        Date dt2;

        try {
            dt1 = sdf.parse(pluginDate);
            dt2 = sdf.parse(ofDate);
            diff = Math.abs(dt2.getTime() - dt1.getTime());
        } catch (ParseException pe) {
            return (long) -1;    //Error
        }
        return diff;
    }*/

    public Long datesMilliesDiff(Date pluginDate, Date ofDate) {
        return Math.abs(pluginDate.getTime() - ofDate.getTime());
    }
}
