package com.machine.project;

import java.sql.Connection;

import javax.inject.Inject;
import javax.sql.DataSource;
 
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

@ContextConfiguration(locations = { "file:src/main/webapp/WEB-INF/spring/**/root-context.xml" })
public class MySQLConnectionTest {

}
