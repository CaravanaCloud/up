package up.producer;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import javax.enterprise.inject.Produces;
import javax.enterprise.inject.spi.InjectionPoint;

public class LoggerProducer {
    @Produces
    @SuppressWarnings("unused")
    Logger produceLogger(InjectionPoint ip) {
        var ipName = ip.getMember().getDeclaringClass().getName();
        return LoggerFactory.getLogger(loggerName(ipName));
    }

    private String loggerName(String ipName) {
        return ipName.substring(ipName.indexOf(".")+1).toLowerCase();
    }
}
