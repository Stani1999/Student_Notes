import java.time.format.DateTimeFormatter;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;


public class kalendarz {

    public static void main(String[] args) {

        GregorianCalendar gc = new GregorianCalendar(2025,10-1,05);
                Date d = gc.getTime();
        System.out.println(d);
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd-MM-YYYY");
        System.out.println(gc.toZonedDateTime().format(dtf));
    }
}