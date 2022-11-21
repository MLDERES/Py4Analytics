



CREATE TABLE Entity_Type
(
    Entity_Type_Id   int         NOT NULL,
    Entity_Type      varchar(30) NOT NULL,

    CONSTRAINT pk_Entity_Type PRIMARY KEY CLUSTERED (Entity_Type_Id)
)
go


insert into Entity_Type ( Entity_Type_Id,Entity_Type) values ( 1,'Agent')
insert into Entity_Type ( Entity_Type_Id,Entity_Type) values ( 2,'Album')
insert into Entity_Type ( Entity_Type_Id,Entity_Type) values ( 3,'Band')
insert into Entity_Type ( Entity_Type_Id,Entity_Type) values ( 4,'Customer')
insert into Entity_Type ( Entity_Type_Id,Entity_Type) values ( 5,'Follower')
insert into Entity_Type ( Entity_Type_Id,Entity_Type) values ( 6,'Genre')
insert into Entity_Type ( Entity_Type_Id,Entity_Type) values ( 7,'Member')
insert into Entity_Type ( Entity_Type_Id,Entity_Type) values ( 8,'Order')
insert into Entity_Type ( Entity_Type_Id,Entity_Type) values ( 9,'Performance')
insert into Entity_Type ( Entity_Type_Id,Entity_Type) values (10,'Playlist')
insert into Entity_Type ( Entity_Type_Id,Entity_Type) values (11,'Producer')
insert into Entity_Type ( Entity_Type_Id,Entity_Type) values (12,'Profile')
insert into Entity_Type ( Entity_Type_Id,Entity_Type) values (13,'Song')
insert into Entity_Type ( Entity_Type_Id,Entity_Type) values (14,'Stream')
insert into Entity_Type ( Entity_Type_Id,Entity_Type) values (15,'Video')
go



CREATE TABLE Persona_Type
(
    Persona_Type_Id   int         NOT NULL,
    Persona_Type      varchar(30) NOT NULL,

    CONSTRAINT pk_Persona_Type PRIMARY KEY CLUSTERED (Persona_Type_Id)
)
go

insert into Persona_Type ( Persona_Type_Id,Persona_Type) values ( 1,'Album')
insert into Persona_Type ( Persona_Type_Id,Persona_Type) values ( 2,'Band')
insert into Persona_Type ( Persona_Type_Id,Persona_Type) values ( 9,'Customer')
insert into Persona_Type ( Persona_Type_Id,Persona_Type) values (11,'Employee')
insert into Persona_Type ( Persona_Type_Id,Persona_Type) values (10,'Experience')
insert into Persona_Type ( Persona_Type_Id,Persona_Type) values ( 3,'Fan')
insert into Persona_Type ( Persona_Type_Id,Persona_Type) values ( 4,'Music')
insert into Persona_Type ( Persona_Type_Id,Persona_Type) values ( 5,'Musician')
insert into Persona_Type ( Persona_Type_Id,Persona_Type) values ( 6,'Performance')
insert into Persona_Type ( Persona_Type_Id,Persona_Type) values (12,'Person')
insert into Persona_Type ( Persona_Type_Id,Persona_Type) values ( 7,'Song')
insert into Persona_Type ( Persona_Type_Id,Persona_Type) values ( 8,'Video')
go


CREATE TABLE Trend_Type
(
    Trend_Type_Id    int         NOT NULL,
    Trend_Type        varchar(30) NOT NULL,

    CONSTRAINT pk_Trend_Type PRIMARY KEY CLUSTERED (Trend_Type_Id)
)
go

insert into trend_type ( Trend_Type_Id, Trend_Type ) values ( 1, 'Default' )


CREATE TABLE Persona
(
    Persona_Id        int         NOT NULL,
    Persona_Type_Id   int         NOT NULL,
    Persona_Name      varchar(30) NOT NULL,

    CONSTRAINT pk_Persona PRIMARY KEY CLUSTERED (Persona_Id)
)
go
CREATE UNIQUE INDEX idx_Persona_Name ON Persona (Persona_Name, Persona_Type_Id)
go
ALTER TABLE Persona ADD CONSTRAINT fk_Persona_Type FOREIGN KEY (Persona_Type_Id) REFERENCES Persona_Type (Persona_Type_Id)
go

insert into persona (persona_id, persona_type_id,Persona_name ) values (1 ,1, 'Bomb')
insert into persona (persona_id, persona_type_id,Persona_name ) values (2 ,1, 'Non-Certified')
insert into persona (persona_id, persona_type_id,Persona_name ) values (3 ,1, 'Gold')
insert into persona (persona_id, persona_type_id,Persona_name ) values (4 ,1, 'Platinum')
insert into persona (persona_id, persona_type_id,Persona_name ) values (35 ,1, 'Multi Platinum')
insert into persona (persona_id, persona_type_id,Persona_name ) values (36 ,1, 'Diamond')
go
insert into persona (persona_id, persona_type_id,Persona_name ) values (5 ,2, 'Bar Band')
insert into persona (persona_id, persona_type_id,Persona_name ) values (6 ,2, 'Cover')
insert into persona (persona_id, persona_type_id,Persona_name ) values (7 ,2, 'Tribute')
insert into persona (persona_id, persona_type_id,Persona_name ) values (8 ,2, '1 hit wonder')
insert into persona (persona_id, persona_type_id,Persona_name ) values (9 ,2, 'Popular')
insert into persona (persona_id, persona_type_id,Persona_name ) values (10 ,2, 'Cult Following')
insert into persona (persona_id, persona_type_id,Persona_name ) values (11 ,2, 'Megaband')
go
insert into persona (persona_id, persona_type_id,Persona_name ) values (12 ,3, 'Casual')
insert into persona (persona_id, persona_type_id,Persona_name ) values (13 ,3, 'Fan')
insert into persona (persona_id, persona_type_id,Persona_name ) values (14 ,3, 'Fanatic')
go
insert into persona (persona_id, persona_type_id,Persona_name ) values (15 ,4, 'Popular')
insert into persona (persona_id, persona_type_id,Persona_name ) values (16 ,4, 'Regional')
insert into persona (persona_id, persona_type_id,Persona_name ) values (17 ,4, 'Seasonal')
insert into persona (persona_id, persona_type_id,Persona_name ) values (18 ,4, 'Specialty')
insert into persona (persona_id, persona_type_id,Persona_name ) values (19 ,4, 'Nostalgic')
go
insert into persona (persona_id, persona_type_id,Persona_name ) values (20 ,5, 'Amateur')
insert into persona (persona_id, persona_type_id,Persona_name ) values (21 ,5, 'Studio')
insert into persona (persona_id, persona_type_id,Persona_name ) values (22 ,5, 'Backup')
insert into persona (persona_id, persona_type_id,Persona_name ) values (23 ,5, 'Lead')
insert into persona (persona_id, persona_type_id,Persona_name ) values (24 ,5, 'Superstar')
go
insert into persona (persona_id, persona_type_id,Persona_name ) values (25 ,6, 'Bad')
insert into persona (persona_id, persona_type_id,Persona_name ) values (26 ,6, 'Good')
insert into persona (persona_id, persona_type_id,Persona_name ) values (27 ,6, 'Epic')
go
insert into persona (persona_id, persona_type_id,Persona_name ) values (28 ,7, 'Bad')
insert into persona (persona_id, persona_type_id,Persona_name ) values (29 ,7, 'Good')
insert into persona (persona_id, persona_type_id,Persona_name ) values (30 ,7, 'Popular')
insert into persona (persona_id, persona_type_id,Persona_name ) values (31 ,7, 'Hit')
go
insert into persona (persona_id, persona_type_id,Persona_name ) values (32 ,8, 'Bad')
insert into persona (persona_id, persona_type_id,Persona_name ) values (33 ,8, 'Good')
insert into persona (persona_id, persona_type_id,Persona_name ) values (34 ,8, 'Viral')
go
insert into persona (persona_id, persona_type_id,Persona_name ) values (37 ,9, 'Occasioanl')
insert into persona (persona_id, persona_type_id,Persona_name ) values (38 ,9, 'Discount')
insert into persona (persona_id, persona_type_id,Persona_name ) values (39 ,9, 'Loyal')
go
insert into persona (persona_id, persona_type_id,Persona_name ) values (40 ,10, 'Bad')
insert into persona (persona_id, persona_type_id,Persona_name ) values (41 ,10, 'Good')
insert into persona (persona_id, persona_type_id,Persona_name ) values (42 ,10, 'Wonderful')
go
insert into persona (persona_id, persona_type_id,Persona_name ) values (43 ,11, 'Bad')
insert into persona (persona_id, persona_type_id,Persona_name ) values (44 ,11, 'Good')
insert into persona (persona_id, persona_type_id,Persona_name ) values (45 ,11, 'Overachiever')
go
insert into persona (persona_id, persona_type_id,Persona_name ) values (46 ,12, 'Student')
insert into persona (persona_id, persona_type_id,Persona_name ) values (47 ,12, 'Young Adult')
insert into persona (persona_id, persona_type_id,Persona_name ) values (48 ,12, 'Mature')
go


CREATE TABLE Persona_Trend
(
    Persona_Id      int         NOT NULL,
    Trend_Type_Id   int         NOT NULL,
    Start_Date      date        NOT NULL,

    End_Date        date            NULL,

    Percent_Market  decimal(10,5)   NULL,
    Average_Dollar  money           NULL,
    Average_Units   int             NULL,
    Average_Days    smallint        NULL,

    Field_Definitions varchar(1000)    NULL,

    CONSTRAINT pk_Persona_Trend PRIMARY KEY CLUSTERED (Persona_Id, Trend_Type_Id, Start_Date)
)
go
ALTER TABLE Persona_Trend ADD CONSTRAINT fk_Persona_Trend_Persona FOREIGN KEY (Persona_Id) REFERENCES Persona (Persona_Id)
go
ALTER TABLE Persona_Trend ADD CONSTRAINT fk_Persona_Trend_Trend FOREIGN KEY (Trend_Type_Id) REFERENCES Trend_Type (Trend_Type_Id)
go

-- album default trend


insert into Persona_Trend (persona_id, trend_type_id, start_date, Average_units ) select 1, 1, '1/1/2000', 100000     -- Bomb
insert into Persona_Trend (persona_id, trend_type_id, start_date, Average_units ) select 2, 1, '1/1/2000', 250000   -- Non-Certified
insert into Persona_Trend (persona_id, trend_type_id, start_date, Average_units ) select 3, 1, '1/1/2000', 500000   -- Gold
insert into Persona_Trend (persona_id, trend_type_id, start_date, Average_units ) select 4, 1, '1/1/2000', 1000000  -- Platinum
insert into Persona_Trend (persona_id, trend_type_id, start_date, Average_units ) select 35, 1,'1/1/2000', 2000000  -- Multi Platinum
insert into Persona_Trend (persona_id, trend_type_id, start_date, Average_units ) select 36, 1,'1/1/2000', 10000000  -- Diamond
go



CREATE TABLE Persona_Entity
(
    Persona_Id        int         NOT NULL,
    Entity_Id         int         NOT NULL,
    Entity_Type_Id    int         NOT NULL,

    CONSTRAINT pk_Persona_Entity PRIMARY KEY CLUSTERED (Persona_Id, Entity_Type_Id, Entity_Id )
)
go
CREATE INDEX idx_Persona_Entity_Entity ON Persona_Entity (Entity_Id)
go
ALTER TABLE Persona_Entity ADD CONSTRAINT fk_Persona_Entity_Persona FOREIGN KEY (Persona_Id) REFERENCES Persona (Persona_Id)
go
ALTER TABLE Persona_Entity ADD CONSTRAINT fk_Persona_Entity_Type FOREIGN KEY (Entity_Type_Id) REFERENCES Entity_Type (Entity_Type_Id)
go




IF OBJECT_ID('dbo.prc_set_Persona') IS NOT NULL
BEGIN
    DROP PROCEDURE dbo.prc_set_Persona
    IF OBJECT_ID('dbo.prc_set_Persona') IS NOT NULL
        PRINT '<<< FAILED DROPPING PROCEDURE dbo.prc_set_Persona >>>'
    ELSE
        PRINT '<<< DROPPED PROCEDURE dbo.prc_set_Persona >>>'
END
go
Create Proc dbo.prc_set_Persona ( @a_Entity_Type varchar(30), @a_Entity_Id int, @a_Persona_Type varchar(30) , @a_Persona varchar(30) ) 
As 
Begin 
 
/*----------------------------------------------------------------------------- 
  Procedure Name: prc_set_Persona

       Function: Populate the persona table
       Parameters: a_Entity_Type, a_Entity_Id, a_Persona_Type, a_Persona
                 
   Modifications:  
 
	11/18/2022	JDS	Initial Version

 -----------------------------------------------------------------------------*/ 


  DECLARE @errorMsg		varchar(255)
	, @errorNum 		int
	, @RowCount 		int
	, @Entity_Type_Id	int
	, @Persona_Type_Id	int
	, @Persona_Id		int


  -- Initialization										 

  SELECT @errorNum = 0



  select @Entity_Type_Id = Entity_Type_Id from Entity_Type where Entity_Type = @a_Entity_Type

  if @Entity_Type_Id is null
  BEGIN 
    SELECT @errorMsg = 'Unknown Entity Type.' 
    GOTO err_rtn
  END 

  select @Persona_Type_Id = Persona_Type_Id from Persona_Type where Persona_Type = @a_Persona_Type

  if @Persona_Type_Id is null
  BEGIN 
    SELECT @errorMsg = 'Unknown Persona Type.' 
    GOTO err_rtn
  END 

  select @Persona_Id = Persona_Id from Persona where Persona_Name = @a_Persona and Persona_Type_Id = @Persona_Type_Id

  if @Persona_Id is null
  BEGIN 
    SELECT @errorMsg = 'Unknown Persona.' 
    GOTO err_rtn
  END 

  if not exists ( select 1 from Persona_Entity where Entity_Id = @a_Entity_Id and Entity_Type_Id = @Entity_Type_Id)
  begin 

    insert into Persona_Entity ( Persona_Id, Entity_Id, Entity_Type_Id ) values (@Persona_Id, @a_Entity_Id, @Entity_Type_Id )

    SELECT @errorNum = @@error , @Rowcount = @@Rowcount
 
    IF @errorNum != 0 or @Rowcount = 0
    BEGIN 
      SELECT @errorMsg = 'Failed inserting row into Persona_Entity.' 
      GOTO err_rtn
    END 

  end    
  else
  begin

    update Persona_Entity set Persona_Id = @Persona_Id 
     where Entity_Id      = @a_Entity_Id
       and Entity_Type_Id = @Entity_Type_Id

    SELECT @errorNum = @@error , @Rowcount = @@Rowcount
 
    IF @errorNum != 0 or @Rowcount = 0
    BEGIN 
      SELECT @errorMsg = 'Update of Persona_Entity failed.' 
      GOTO err_rtn
    END 


  end

good_rtn: 
 
  Return 0

err_rtn: 

  select @errorMsg = 'SQL Exception (' + object_name(@@procid) + ') - ' + @errorMsg + case when IsNull(@errornum,0) <> 0 then ' (SQL Errno: ' + convert(varchar(30),@errorNum) + ')' else null end

  --RAISERROR 50001 @errorMsg 
  Return -1 
  
End /* prc_set_Persona */
go

IF OBJECT_ID('dbo.prc_set_Persona') IS NOT NULL
    PRINT '<<< CREATED PROCEDURE dbo.prc_set_Persona >>>'
ELSE
    PRINT '<<< FAILED CREATING PROCEDURE dbo.prc_set_Persona >>>'
go
grant exec on prc_set_Persona to jds_user
go





CREATE TABLE Platform 
(
    Platform_Id        int         NOT NULL,
    Platform_Name      varchar(30) NOT NULL,

    URL                varchar(500) NULL,

    CONSTRAINT pk_Platform PRIMARY KEY CLUSTERED (Platform_Id)
)
go
CREATE UNIQUE INDEX idx_Platform_Name ON Platform (Platform_Name)
go



insert into Platform (platform_id, Platform_name, URL ) values (1, 'Apple Music','https://www.apple.com/apple-music/')
insert into Platform (platform_id, Platform_name, URL ) values (2, 'Amazon Music','https://music.amazon.com/')
insert into Platform (platform_id, Platform_name, URL ) values (3, 'Hallux Music','')
insert into Platform (platform_id, Platform_name, URL ) values (4, 'iHeartRadio','https://www.iheart.com/')
insert into Platform (platform_id, Platform_name, URL ) values (5, 'Pandora','https://www.pandora.com/')
insert into Platform (platform_id, Platform_name, URL ) values (6, 'Spotify','https://open.spotify.com/')
insert into Platform (platform_id, Platform_name, URL ) values (7, 'SoundClooud','https://soundcloud.com/')
insert into Platform (platform_id, Platform_name, URL ) values (8, 'Tidal','https://tidal.com/')
insert into Platform (platform_id, Platform_name, URL ) values (9, 'YouTube Music','https://music.youtube.com/')






CREATE TABLE Band_Follower
(
    Follower_Id    int         NOT NULL,

    Band_Id        int         NOT NULL,
    Profile_Id     int         NOT NULL,
    Follow_Date    Datetime    NOT NULL,

    Unfollow_Date  Datetime        NULL,


    CONSTRAINT pk_Band_Follower PRIMARY KEY NONCLUSTERED (Follower_Id)
)
go
CREATE UNIQUE CLUSTERED INDEX idx_Band_Follower ON Band_Follower (Band_Id, Profile_Id, Follow_Date)
go
ALTER TABLE Band_Follower ADD CONSTRAINT fk_Band_Follower_Band  FOREIGN KEY (Band_Id) REFERENCES Band (Band_Id)
go
ALTER TABLE Band_Follower ADD CONSTRAINT fk_Band_Follower_Profile FOREIGN KEY (Profile_Id) REFERENCES Customer_Profile (Profile_Id)
go




CREATE TABLE Playlist
(
    Playlist_Id        int         NOT NULL,
    Playlist_Name      varchar(30) NOT NULL,

    Description        varchar(100)    NULL,
    Owner_Id           int             NULL,
    Genre_Id           int             NULL,
    Private            binary          NULL,

    CONSTRAINT pk_Playlist PRIMARY KEY CLUSTERED (Playlist_Id)
)
go
CREATE UNIQUE INDEX idx_Playlist_Name ON Playlist (Playlist_Name)
go
ALTER TABLE Playlist ADD CONSTRAINT fk_Playlist_Genre FOREIGN KEY (Genre_Id) REFERENCES Genre (Genre_Id)
go
ALTER TABLE Playlist ADD CONSTRAINT fk_Playlist_Owner FOREIGN KEY (Owner_Id) REFERENCES Customer_Profile (Profile_Id)
go

CREATE TABLE Playlist_Song
(
    Playlist_Id        int         NOT NULL,
    Song_Id            int         NOT NULL,

    Sequence           tinyint         NULL,

    CONSTRAINT pk_Playlist_Song PRIMARY KEY CLUSTERED (Playlist_Id, Song_Id)
)
go
ALTER TABLE Playlist_Song ADD CONSTRAINT fk_Playlist_Song_Song  FOREIGN KEY (Song_Id) REFERENCES Song (Song_Id)
go
ALTER TABLE Playlist_Song ADD CONSTRAINT fk_Playlist_Song_Playlist FOREIGN KEY (Playlist_Id) REFERENCES Playlist (Playlist_Id)
go

CREATE TABLE Customer_Playlist
(
    Profile_Id         int         NOT NULL,
    Playlist_Id        int         NOT NULL,

    Rating             tinyint         NULL,

    CONSTRAINT pk_Customer_Playlist PRIMARY KEY CLUSTERED (Profile_Id, Playlist_Id)
)
go
ALTER TABLE Customer_Playlist ADD CONSTRAINT fk_Customer_Playlist_Profile FOREIGN KEY (Profile_Id) REFERENCES Customer_Profile (Profile_Id)
go
ALTER TABLE Customer_Playlist ADD CONSTRAINT fk_Customer_Playlist_Playlist FOREIGN KEY (Playlist_Id) REFERENCES Playlist (Playlist_Id)
go


CREATE TABLE Stream
(
    Stream_Id      int         NOT NULL,

    Stream_Date    Datetime    NOT NULL,
    Item_Id        int         NOT NULL,
    Platform_Id    int         NOT NULL,
    Profile_Id     int             NULL,
    Stream_End     Datetime        NULL,

    CONSTRAINT pk_Stream PRIMARY KEY NONCLUSTERED (Stream_Id)
)
go
ALTER TABLE Stream ADD CONSTRAINT fk_Stream_Item  FOREIGN KEY (Item_Id) REFERENCES Item (Item_Id)
go
ALTER TABLE Stream ADD CONSTRAINT fk_Stream_Platform FOREIGN KEY (Platform_Id) REFERENCES Platform (Platform_Id)
go
ALTER TABLE Stream ADD CONSTRAINT fk_Stream_Profile FOREIGN KEY (Profile_Id) REFERENCES Customer_Profile (Profile_Id)
go
CREATE UNIQUE CLUSTERED INDEX idx_Stream ON Stream (Item_Id, Stream_Date, Platform_Id)
go
CREATE INDEX idx_Stream_Date ON Stream (Stream_Date)
go






CREATE TABLE Date_Mapping
(
    Hax_Date        Date NOT NULL,
    Hax_Date_End    Datetime NULL,
    Adj_Date        Date     NULL,
    Adj_Weekday     Date     NULL,
    Holiday         Char(10) NULL,

    CONSTRAINT pk_Date_Mapping PRIMARY KEY CLUSTERED (Hax_Date)
)
go



IF OBJECT_ID('dbo.prc_Date_Mapping_Retrieve') IS NOT NULL
BEGIN
    DROP PROCEDURE dbo.prc_Date_Mapping_Retrieve
    IF OBJECT_ID('dbo.prc_Date_Mapping_Retrieve') IS NOT NULL
        PRINT '<<< FAILED DROPPING PROCEDURE dbo.prc_Date_Mapping_Retrieve >>>'
    ELSE
        PRINT '<<< DROPPED PROCEDURE dbo.prc_Date_Mapping_Retrieve >>>'
END
go
Create Proc dbo.prc_Date_Mapping_Retrieve ( @a_From_Date date , @a_To_Date date)
As 
Begin 
 
/*----------------------------------------------------------------------------- 
  Procedure Name: prc_Date_Mapping_Retrieve 

   Function: Return Date_Mapping data for the specified date range.
   Parameters:  @a_From_Date, @a_To_Date
                 
   Modifications:  
 
	10/04/2022	JDS	Initial Version

 -----------------------------------------------------------------------------*/ 


  select Hax_Date
	,Adj_Date
	,Adj_Weekday
	,Holiday
	,Hax_Date_End

  from Date_Mapping 
  where Hax_Date between @a_From_Date and @a_To_Date

  
End /* prc_Date_Mapping_Retrieve */
go

IF OBJECT_ID('dbo.prc_Date_Mapping_Retrieve') IS NOT NULL
    PRINT '<<< CREATED PROCEDURE dbo.prc_Date_Mapping_Retrieve >>>'
ELSE
    PRINT '<<< FAILED CREATING PROCEDURE dbo.prc_Date_Mapping_Retrieve >>>'
go




-- exec prc_Date_Mapping_Populate

IF OBJECT_ID('dbo.prc_Date_Mapping_Populate') IS NOT NULL
BEGIN
    DROP PROCEDURE dbo.prc_Date_Mapping_Populate
    IF OBJECT_ID('dbo.prc_Date_Mapping_Populate') IS NOT NULL
        PRINT '<<< FAILED DROPPING PROCEDURE dbo.prc_Date_Mapping_Populate >>>'
    ELSE
        PRINT '<<< DROPPED PROCEDURE dbo.prc_Date_Mapping_Populate >>>'
END
go
Create Proc dbo.prc_Date_Mapping_Populate 
As 
Begin 
 
/*----------------------------------------------------------------------------- 
  Procedure Name: prc_Date_Mapping_Populate 

   Function: Populate Date_Mapping table with all unique dates in the database
   Parameters:  None
                 
   Modifications:  
 
	10/01/2022	JDS	Initial Version

 -----------------------------------------------------------------------------*/ 

  
  DECLARE @errorMsg	varchar(255)
	, @errorNum 	int
	, @Rowcount 	int

 
  -- Initialization										 

  SELECT @errorNum = 0

  Delete from Date_Mapping

  SELECT @errorNum = @@error , @Rowcount = @@Rowcount
 
  IF @errorNum != 0 
  BEGIN 
    SELECT @errorMsg = 'Delete of Date_Mapping failed.'
    GOTO err_rtn 
  END 

  insert into Date_Mapping (Hax_Date)

         select distinct convert(date,hire_date) from agent where hire_date is not null
   union select distinct convert(date,release_date) from album where release_date is not null
   union select distinct convert(date,formation_date) from band where formation_date is not null
   union select distinct convert(date,join_date) from band_member where join_date is not null
   union select distinct convert(date,end_date) from contract where end_date is not null
   union select distinct convert(date,begin_date) from contract where begin_date is not null
   union select distinct convert(date,order_date) from order_header where order_date is not null
   union select distinct convert(date,promise_date) from order_header where promise_date is not null
   union select distinct convert(date,performance_date) from performance where performance_date is not null
   union select distinct convert(date,birthdate) from customer_profile where birthdate is not null

  
  SELECT @errorNum = @@error , @Rowcount = @@Rowcount
 
  IF @errorNum != 0 
  BEGIN 
    SELECT @errorMsg = 'Insert into Date_Mapping failed.'
    GOTO err_rtn
  END 


  update Date_Mapping set   Hax_Date_End  = convert(datetime,convert(varchar(20), Hax_Date , 101 ) + ' 23:59:59:990')


  SELECT @errorNum = @@error , @Rowcount = @@Rowcount
 
  IF @errorNum != 0 
  BEGIN 
    SELECT @errorMsg = 'Error updating Hax_Date_End.'
    GOTO err_rtn
  END 
 
good_rtn: 
 
  Return 0 

err_rtn: 

  select @errorMsg = 'SQL Exception (' + object_name(@@procid) + ') - ' + @errorMsg + case when IsNull(@errornum,0) <> 0 then ' (SQL Errno: ' + convert(varchar(30),@errorNum) + ')' else null end

  --RAISERROR 50001 @errorMsg 
  Return -1 
  
End /* prc_Date_Mapping_Populate */
go

IF OBJECT_ID('dbo.prc_Date_Mapping_Populate') IS NOT NULL
    PRINT '<<< CREATED PROCEDURE dbo.prc_Date_Mapping_Populate >>>'
ELSE
    PRINT '<<< FAILED CREATING PROCEDURE dbo.prc_Date_Mapping_Populate >>>'
go





IF OBJECT_ID('dbo.prc_Date_Mapping_Adjust') IS NOT NULL
BEGIN
    DROP PROCEDURE dbo.prc_Date_Mapping_Adjust
    IF OBJECT_ID('dbo.prc_Date_Mapping_Adjust') IS NOT NULL
        PRINT '<<< FAILED DROPPING PROCEDURE dbo.prc_Date_Mapping_Adjust >>>'
    ELSE
        PRINT '<<< DROPPED PROCEDURE dbo.prc_Date_Mapping_Adjust >>>'
END
go
Create Proc dbo.prc_Date_Mapping_Adjust ( @a_NumYears smallint = 1 )
As 
Begin 
 
/*----------------------------------------------------------------------------- 
  Procedure Name: prc_Date_Mapping_Adjust 

   Function: Set the adjusted dates in Date_Mapping
   Parameters:  @a_NumYears
                 
   Modifications:  
 
	10/01/2022	JDS	Initial Version

 -----------------------------------------------------------------------------*/ 

  
  DECLARE @errorMsg	varchar(255)
	, @errorNum 	int
	, @Rowcount 	int
	, @cnt	 	int

 
  -- Initialization										 

  SELECT @errorNum = 0


  -- set Adj_Date
  UPDATE Date_Mapping set Adj_Date = dateadd( year, @a_NumYears , Hax_Date ), Holiday = null 

  SELECT @errorNum = @@error , @Rowcount = @@Rowcount
 
  IF @errorNum != 0 
  BEGIN 
    SELECT @errorMsg = 'Update of Adj_Date failed.'
    GOTO err_rtn 
  END 


  --  identify holidays

  create table #temp_holiday (

	 Holiday           Char(10) NULL
	,Month             tinyint  NULL
	,Weekday           tinyint  NULL
	,Day_Range_Begin   tinyint  NULL
	,Day_Range_End     tinyint  NULL
	)

  -- fixed holidays
  insert into #temp_holiday values ( 'FIXED' ,1 , null, 1 , 1 ) -- New Year's Day
  insert into #temp_holiday values ( 'FIXED' ,6 , null, 19 ,19) -- Juneteenth National Independence Day
  insert into #temp_holiday values ( 'FIXED' ,7 , null, 4 , 4 ) -- Independence Day
  insert into #temp_holiday values ( 'FIXED' ,10, null, 31, 31) -- Holloween
  insert into #temp_holiday values ( 'FIXED' ,11, null, 11, 11) -- Veterans Day
  insert into #temp_holiday values ( 'FIXED' ,12, null, 24, 24) -- Christmas Eve
  insert into #temp_holiday values ( 'FIXED' ,12, null, 25, 25) -- Christmas Day
  insert into #temp_holiday values ( 'FIXED' ,12, null, 31, 31) -- New Year’s Eve

  -- floating holidays

  insert into #temp_holiday values ( 'FLOATING', 1 , 2, 15, 21) -- Martin Luther King , Jr. Birthday
  insert into #temp_holiday values ( 'FLOATING', 2 , 2, 15, 21) -- Washington's Birthday
  insert into #temp_holiday values ( 'FLOATING', 5 , 2, 25, 31) -- Memorial Day
  insert into #temp_holiday values ( 'FLOATING', 9 , 2, 1 , 7 ) -- Labor Day
  insert into #temp_holiday values ( 'FLOATING', 10, 2, 8 , 14) -- Columbus Day
  insert into #temp_holiday values ( 'FLOATING', 11, 5, 22, 28) -- Thanksgiving Day


  UPDATE Date_Mapping set Holiday = t.Holiday
    from Date_Mapping m
       , #temp_holiday t
   where datepart(month  ,m.Hax_Date) = t.Month
     and datepart(day    ,m.Hax_Date) between t.Day_Range_Begin and t.Day_Range_End
     and (t.Weekday is null or datepart(weekday,m.Hax_Date) = t.Weekday) 

  SELECT @errorNum = @@error , @Rowcount = @@Rowcount
 
  IF @errorNum != 0 
  BEGIN 
    SELECT @errorMsg = 'Update of Holiday failed.'
    GOTO err_rtn
  END 

  -- set Adj_Weekday to have the same day of the week of Hax_Date 
  UPDATE Date_Mapping set Adj_Weekday =  dateadd( day, datepart(weekday,Hax_Date) - datepart(weekday,Adj_Date) , Adj_Date) 

  SELECT @errorNum = @@error , @Rowcount = @@Rowcount
 
  IF @errorNum != 0 
  BEGIN 
    SELECT @errorMsg = 'Update of Adj_Weekday failed.'
    GOTO err_rtn
  END 
  

  -- make sure the new floating holiday is in the appropriate date range

  UPDATE Date_Mapping set Adj_Weekday =  dateadd( day, 7, Adj_Weekday) 
    from Date_Mapping m
       , #temp_holiday t
   where m.Holiday = 'FLOATING'
     and datepart(month ,m.Hax_Date) = t.Month
     and datepart(day   ,m.Hax_Date) between t.Day_Range_Begin and t.Day_Range_End
     and datepart(day   ,m.Adj_Holiday) < t.Day_Range_Begin

  SELECT @errorNum = @@error , @Rowcount = @@Rowcount
 
  IF @errorNum != 0 
  BEGIN 
    SELECT @errorMsg = 'Update of Floating Adj_Weekday failed.'
    GOTO err_rtn
  END 
  
 
good_rtn: 
 
  Return 0 

err_rtn: 

  select @errorMsg = 'SQL Exception (' + object_name(@@procid) + ') - ' + @errorMsg + case when IsNull(@errornum,0) <> 0 then ' (SQL Errno: ' + convert(varchar(30),@errorNum) + ')' else null end

  --RAISERROR 50001 @errorMsg 
  Return -1 
  
End /* prc_Date_Mapping_Adjust */
go

IF OBJECT_ID('dbo.prc_Date_Mapping_Adjust') IS NOT NULL
    PRINT '<<< CREATED PROCEDURE dbo.prc_Date_Mapping_Adjust >>>'
ELSE
    PRINT '<<< FAILED CREATING PROCEDURE dbo.prc_Date_Mapping_Adjust >>>'
go






IF OBJECT_ID('dbo.prc_Date_Mapping_Update') IS NOT NULL
BEGIN
    DROP PROCEDURE dbo.prc_Date_Mapping_Update
    IF OBJECT_ID('dbo.prc_Date_Mapping_Update') IS NOT NULL
        PRINT '<<< FAILED DROPPING PROCEDURE dbo.prc_Date_Mapping_Update >>>'
    ELSE
        PRINT '<<< DROPPED PROCEDURE dbo.prc_Date_Mapping_Update >>>'
END
go
Create Proc dbo.prc_Date_Mapping_Update ( @a_Hax_Date date, @a_Adj_Date Date, @a_Adj_Weekday date, @a_Holiday Char(10) )
As 
Begin 
 
    
/*----------------------------------------------------------------------------- 
  Procedure Name: prc_Date_Mapping_Update 

   Function: Updates or inserts a row in Date_Mapping
   Parameters:  @a_NumYears
                 
   Modifications:  
 
	10/04/2022	JDS	Initial Version

 -----------------------------------------------------------------------------*/ 

  
  DECLARE @errorMsg	varchar(255)
	, @errorNum 	int
	, @Rowcount 	int

 
  -- Initialization										 

  SELECT @errorNum = 0

  IF @a_Hax_Date is null
  BEGIN 
    SELECT @errorMsg = 'Hax_Date is required.' 
    GOTO err_rtn 
  END 


  -- insert or update

  if exists ( select 1 from Date_Mapping where Hax_Date = @a_Hax_Date )

    UPDATE Date_Mapping set Adj_Date = IsNull(@a_Adj_Date,Adj_Date),  Adj_Weekday = IsNull(@a_Adj_Weekday, Adj_Weekday), Holiday = @a_Holiday where Hax_Date = @a_Hax_Date

  ELSE

    INSERT into Date_Mapping ( Hax_Date, Adj_Date, Adj_Weekday, Holiday ) values ( @a_Hax_Date, @a_Adj_Date, @a_Adj_Weekday, @a_Holiday )


  SELECT @errorNum = @@error , @Rowcount = @@Rowcount
 
  IF @errorNum != 0 or @Rowcount = 0
  BEGIN 
    SELECT @errorMsg = 'Insert/Update of Date_Mapping failed.'
    GOTO err_rtn 
  END 

 
good_rtn: 
 
  Return 0 

err_rtn: 

  select @errorMsg = 'SQL Exception (' + object_name(@@procid) + ') - ' + @errorMsg + case when IsNull(@errornum,0) <> 0 then ' (SQL Errno: ' + convert(varchar(30),@errorNum) + ')' else null end

  --RAISERROR 50001 @errorMsg 
  Return -1 
  
End /* prc_Date_Mapping_Update */
go

IF OBJECT_ID('dbo.prc_Date_Mapping_Update') IS NOT NULL
    PRINT '<<< CREATED PROCEDURE dbo.prc_Date_Mapping_Update >>>'
ELSE
    PRINT '<<< FAILED CREATING PROCEDURE dbo.prc_Date_Mapping_Update >>>'
go







IF OBJECT_ID('dbo.prc_Date_Mapping_Update_Hax') IS NOT NULL
BEGIN
    DROP PROCEDURE dbo.prc_Date_Mapping_Update_Hax
    IF OBJECT_ID('dbo.prc_Date_Mapping_Update_Hax') IS NOT NULL
        PRINT '<<< FAILED DROPPING PROCEDURE dbo.prc_Date_Mapping_Update_Hax >>>'
    ELSE
        PRINT '<<< DROPPED PROCEDURE dbo.prc_Date_Mapping_Update_Hax >>>'
END
go
Create Proc dbo.prc_Date_Mapping_Update_Hax 
As 
Begin 
 
/*----------------------------------------------------------------------------- 
  Procedure Name: prc_Date_Mapping_Update_Hax 

   Function:  update the database with the adjusted dates in Date_Mapping
   Parameters:  none
                 
   Modifications:  
 
	10/01/2022	JDS	Initial Version

 -----------------------------------------------------------------------------*/ 

  
  DECLARE @errorMsg	varchar(255)
	, @errorNum 	int
	, @Rowcount 	int

 
  -- Initialization										 

  SELECT @errorNum = 0


  update agent set Hire_Date =  convert(datetime, convert(varchar(30), m.Adj_Date, 101 ) + ' ' +  convert(varchar(30), hire_date, 108 ) + ':' + convert(varchar(30), datepart(millisecond,hire_date)))    
    from Date_Mapping m
       , agent t
   where t.Hire_Date between m.Hax_Date and m.Hax_Date_End
    
  SELECT @errorNum = @@error , @Rowcount = @@Rowcount
 
  IF @errorNum != 0 
  BEGIN 
    SELECT @errorMsg = 'Update of Hire_Date failed.'
    GOTO err_rtn 
  END 


  update album set Release_Date =  convert(datetime, convert(varchar(30), m.Adj_Date, 101 ) + ' ' +  convert(varchar(30), Release_date, 108 ) + ':' + convert(varchar(30), datepart(millisecond, Release_date)))    
    from Date_Mapping m
       , album t
   where t.Release_Date between m.Hax_Date and m.Hax_Date_End
    
  SELECT @errorNum = @@error , @Rowcount = @@Rowcount
 
  IF @errorNum != 0 
  BEGIN 
    SELECT @errorMsg = 'Update of Release_Date failed.'
    GOTO err_rtn 
  END 


  update Band set Formation_Date =  convert(datetime, convert(varchar(30), m.Adj_Date, 101 ) + ' ' +  convert(varchar(30), Formation_date, 108 ) + ':' + convert(varchar(30), datepart(millisecond, Formation_date)))    
    from Date_Mapping m
       , Band t
   where t.Formation_Date between m.Hax_Date and m.Hax_Date_End
    
  SELECT @errorNum = @@error , @Rowcount = @@Rowcount
 
  IF @errorNum != 0 
  BEGIN 
    SELECT @errorMsg = 'Update of Formation_Date failed.'
    GOTO err_rtn 
  END 

  update Band_Member set Join_Date =  convert(datetime, convert(varchar(30), m.Adj_Date, 101 ) + ' ' +  convert(varchar(30), Join_Date, 108 ) + ':' + convert(varchar(30), datepart(millisecond, Join_Date)))    
    from Date_Mapping m
       , Band_Member t
   where t.Join_Date between m.Hax_Date and m.Hax_Date_End
    
  SELECT @errorNum = @@error , @Rowcount = @@Rowcount
 
  IF @errorNum != 0 
  BEGIN 
    SELECT @errorMsg = 'Update of Join_Date failed.'
    GOTO err_rtn 
  END 


  update Contract set Begin_Date =  convert(datetime, convert(varchar(30), m.Adj_Date, 101 ) + ' ' +  convert(varchar(30), Begin_Date, 108 ) + ':' + convert(varchar(30), datepart(millisecond, Begin_Date)))    
    from Date_Mapping m
       , Contract t
   where t.Begin_Date between m.Hax_Date and m.Hax_Date_End
    
  SELECT @errorNum = @@error , @Rowcount = @@Rowcount
 
  IF @errorNum != 0 
  BEGIN 
    SELECT @errorMsg = 'Update of Begin_Date failed.'
    GOTO err_rtn 
  END 

  update Contract set End_Date =  convert(datetime, convert(varchar(30), m.Adj_Date, 101 ) + ' ' +  convert(varchar(30), End_Date, 108 ) + ':' + convert(varchar(30), datepart(millisecond, End_Date)))    
    from Date_Mapping m
       , Contract t
   where t.End_Date between m.Hax_Date and m.Hax_Date_End
    
  SELECT @errorNum = @@error , @Rowcount = @@Rowcount
 
  IF @errorNum != 0 
  BEGIN 
    SELECT @errorMsg = 'Update of End_Date failed.'
    GOTO err_rtn 
  END 


  update order_header set Order_Date =  convert(datetime, convert(varchar(30), m.Adj_Date, 101 ) + ' ' +  convert(varchar(30), Order_Date, 108 ) + ':' + convert(varchar(30), datepart(millisecond, Order_Date)))    
    from Date_Mapping m
       , order_header t
   where t.Order_Date between m.Hax_Date and m.Hax_Date_End
    
  SELECT @errorNum = @@error , @Rowcount = @@Rowcount
 
  IF @errorNum != 0 
  BEGIN 
    SELECT @errorMsg = 'Update of Order_Date failed.'
    GOTO err_rtn 
  END 

  update order_header set Promise_Date =  convert(datetime, convert(varchar(30), m.Adj_Date, 101 ) + ' ' +  convert(varchar(30), Promise_Date, 108 ) + ':' + convert(varchar(30), datepart(millisecond, Promise_Date)))    
    from Date_Mapping m
       , order_header t
   where t.Promise_Date between m.Hax_Date and m.Hax_Date_End
    
  SELECT @errorNum = @@error , @Rowcount = @@Rowcount
 
  IF @errorNum != 0 
  BEGIN 
    SELECT @errorMsg = 'Update of Promise_Date failed.'
    GOTO err_rtn 
  END 

  -- maintain the day of the week unless the date is a fixed holiday

  update Performance set Performance_Date =  convert(datetime, convert(varchar(30), case when m.Holiday = 'FIXED' then m.Adj_Date else m.Adj_Weekday end, 101 ) + ' ' +  convert(varchar(30), Performance_Date, 108 ) + ':' + convert(varchar(30), datepart(millisecond, Performance_Date)))    
    from Date_Mapping m
       , Performance t
   where t.Performance_Date between m.Hax_Date and m.Hax_Date_End
    
  SELECT @errorNum = @@error , @Rowcount = @@Rowcount
 
  IF @errorNum != 0 
  BEGIN 
    SELECT @errorMsg = 'Update of Performance_Date failed.'
    GOTO err_rtn 
  END 


  -- birthday is always on the same date

  update customer_profile set birthdate =  convert(datetime, convert(varchar(30), m.Adj_Date, 101 ) + ' ' +  convert(varchar(30), birthdate, 108 ) + ':' + convert(varchar(30), datepart(millisecond, birthdate)))    
    from Date_Mapping m
       , customer_profile t
   where t.Birthdate between m.Hax_Date and m.Hax_Date_End
    
  SELECT @errorNum = @@error , @Rowcount = @@Rowcount
 
  IF @errorNum != 0 
  BEGIN 
    SELECT @errorMsg = 'Update of birthdate failed.'
    GOTO err_rtn 
  END 


 
good_rtn: 
 
  Return 0 

err_rtn: 

  select @errorMsg = 'SQL Exception (' + object_name(@@procid) + ') - ' + @errorMsg + case when IsNull(@errornum,0) <> 0 then ' (SQL Errno: ' + convert(varchar(30),@errorNum) + ')' else null end

  --RAISERROR 50001 @errorMsg 
  Return -1 
  
End /* prc_Date_Mapping_Update_Hax */
go

IF OBJECT_ID('dbo.prc_Date_Mapping_Update_Hax') IS NOT NULL
    PRINT '<<< CREATED PROCEDURE dbo.prc_Date_Mapping_Update_Hax >>>'
ELSE
    PRINT '<<< FAILED CREATING PROCEDURE dbo.prc_Date_Mapping_Update_Hax >>>'
go



IF OBJECT_ID('dbo.prc_Increment_Date') IS NOT NULL
BEGIN
    DROP PROCEDURE dbo.prc_Increment_Date
    IF OBJECT_ID('dbo.prc_Increment_Date') IS NOT NULL
        PRINT '<<< FAILED DROPPING PROCEDURE dbo.prc_Increment_Date >>>'
    ELSE
        PRINT '<<< DROPPED PROCEDURE dbo.prc_Increment_Date >>>'
END
go
Create Proc dbo.prc_Increment_Date ( @a_date_curr date = null , @a_date_new date = null, @a_table varchar(30) = null, @a_column varchar(30) = null) 
As 
Begin 
 
/*----------------------------------------------------------------------------- 
  Procedure Name: prc_Increment_Date 

   Function: Changes the specified date/column/table combination to the new date

   Parameters:  

	a_dt_curr
	a_dt_new
	a_table
	a_column
                 
   Modifications:  
 
	09/30/2022	JDS	Initial Version

 -----------------------------------------------------------------------------*/ 

  
  DECLARE @errorMsg	varchar(255)
	, @sql	 	varchar(1000)
	, @where_clause	varchar(255)
	, @new_time	varchar(255)
	, @new_date	varchar(30)
	, @errorNum 	int
	, @Rowcount 	int
	, @dt_start	datetime
	, @dt_end	datetime

 
  -- Initialization										 

  SELECT @errorNum = 0
  SELECT @dt_start = @a_date_curr
  SELECT @dt_end   = convert(datetime, convert(varchar(30), @dt_start, 101 ) + ' 23:59:59:999') 



/*
  IF ( @a_dt_end < @a_dt_start) 
  BEGIN 
    SELECT @errorMsg = 'End date cannot be prior to Start date.' 
    GOTO err_rtn 
  END 
*/

  -- validate @a_table , @a_column 




  /*
      This is the sql prototype

      update agent        
         set hire_date =  convert(datetime, convert(varchar(30), @a_date_new, 101 ) + ' ' +  convert(varchar(30), hire_date, 108 ) + ':' + convert(varchar(30), datepart(millisecond,hire_date)))    
       where hire_date between @dt_start and @dt_end

    test run

   exec prc_Increment_Date  @a_date_curr = '9/1/22'  , @a_date_new  = '9/2/23', @a_table  = 'agent', @a_column = 'hire_date'

    update agent 
    set hire_date = convert(datetime, "09/02/2023" + " " +  convert(varchar(30), hire_date, 108 ) + ":" + convert(varchar(30), datepart(millisecond,hire_date))) 
    where hire_date between "09/01/2022" and  "09/01/2022 23:59:59:999"

  */


  select @new_date      = convert(varchar(30), @a_date_new, 101 )
      , @new_time =  'convert(varchar(30), '  + @a_column  + ', 108 ) + ":" + convert(varchar(30), datepart(millisecond,'+ @a_column +'))' 
       , @where_clause	= 'where '  + @a_column + ' between "' + convert(varchar(30), @a_date_curr, 101 ) +  '" and  "' + convert(varchar(30),@a_date_curr, 101 ) + ' 23:59:59:999"'


 select @sql = 'update ' + @a_table + ' set ' + @a_column  + ' = convert(datetime, "'  + @new_date + '" + " " +  '  +  @new_time  + ') ' + @where_clause


  --BEGIN TRANSACTION 

    select @sql

  -- execute ( @sql )
  
  SELECT @errorNum = @@error , @Rowcount = @@Rowcount
 
  IF @errorNum != 0 
  BEGIN 
    SELECT @errorMsg = 'Date update failed for ' + @a_table + '.' + @a_column
 --   GOTO roll_rtn 
  END 



  -- COMMIT TRANSACTION 


 
good_rtn: 
 
  Return 0 
 
roll_rtn: 
 
  -- ROLLBACK TRANSACTION 
 
err_rtn: 

  select @errorMsg = 'SQL Exception (' + object_name(@@procid) + ') - ' + @errorMsg + case when IsNull(@errornum,0) <> 0 then ' (SQL Errno: ' + convert(varchar(30),@errorNum) + ')' else null end

  --RAISERROR 50001 @errorMsg 
  Return -1 
  
End /* prc_Increment_Date */
go

IF OBJECT_ID('dbo.prc_Increment_Date') IS NOT NULL
    PRINT '<<< CREATED PROCEDURE dbo.prc_Increment_Date >>>'
ELSE
    PRINT '<<< FAILED CREATING PROCEDURE dbo.prc_Increment_Date >>>'
go










