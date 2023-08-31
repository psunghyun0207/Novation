import pygame
import time

Version = "1.0.0v ALPHA TEST"

# 색 설정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# 초기화
pygame.init()
pygame.mixer.init()

SoundChannel_BGM = pygame.mixer.Channel(1)
SoundChannel_HITSOUND = pygame.mixer.Channel(2)
SoundChannel_EFFECT = pygame.mixer.Channel(3)
SoundChannel_SELECT = pygame.mixer.Channel(4)
SoundChannel_SONGSELECT = pygame.mixer.Channel(5)

# 화면 초기 설정
Screen_Horizon = 1920
w = Screen_Horizon
Screen_Vertical = 1080
h = Screen_Vertical

Screen = pygame.display.set_mode((Screen_Horizon, Screen_Vertical))

# 화면 타이틀 설정
pygame.display.set_caption("NOVATION")

# FPS
clock = pygame.time.Clock()

# 배경화면 불러오기
img_Background_Main = pygame.image.load(r'BG\Background_Main.png')
img_Background_Option = pygame.image.load(r'BG\Background_Option.png')

# 스프라이트 불러오기

    #노트 입력 마커
img_Note_Press = pygame.image.load(r'NOTE\Note_Press.png')

    #노트 프레임 이미지
img_Note_Frame = [
                pygame.image.load(r'NOTE\Note_Frame_1.png'),
                pygame.image.load(r'NOTE\Note_Frame_2.png'),
                pygame.image.load(r'NOTE\Note_Frame_3.png'),
                pygame.image.load(r'NOTE\Note_Frame_4.png') #출처 https://kr.lovepik.com/images/png-square.html
                ]

Current_Note_Frame = 0
Note_Frame_Array = 4 - 1

    #판정 이미지
img_Judge_PGREAT = pygame.image.load(r'JUDGE\Judge_100+.png')
img_Judge_GREAT = pygame.image.load(r'JUDGE\Judge_100.png')
img_Judge_GOOD = pygame.image.load(r'JUDGE\Judge_50.png')
img_Judge_MISS = pygame.image.load(r'JUDGE\Judge_Miss.png')

    #메인화면 이미지
img_main_Title = pygame.image.load(r'MAIN\TITLE.png')
img_main_Start_ON = pygame.image.load(r'MAIN\START_ON.png')
img_main_Option_ON = pygame.image.load(r'MAIN\OPTION_ON.png')
img_main_Exit_ON = pygame.image.load(r'MAIN\EXIT_ON.png')
img_main_Start_OFF = pygame.image.load(r'MAIN\START_OFF.png')
img_main_Option_OFF = pygame.image.load(r'MAIN\OPTION_OFF.png')
img_main_Exit_OFF = pygame.image.load(r'MAIN\EXIT_OFF.png')

img_main_Option = pygame.image.load(r'MAIN\OPTION.png')

    #페이드인아웃 이미지
Fade = [
        pygame.image.load(r'FADE\Fade_1.png'),
        pygame.image.load(r'FADE\Fade_2.png'),
        pygame.image.load(r'FADE\Fade_3.png'),
        pygame.image.load(r'FADE\Fade_4.png'),
        pygame.image.load(r'FADE\Fade_5.png'),
        pygame.image.load(r'FADE\Fade_6.png'),
        pygame.image.load(r'FADE\Fade_7.png'),
        pygame.image.load(r'FADE\Fade_8.png'),
        pygame.image.load(r'FADE\Fade_9.png'),
        pygame.image.load(r'FADE\Fade_10.png'),
        pygame.image.load(r'FADE\Fade_9.png'),
        pygame.image.load(r'FADE\Fade_8.png'),
        pygame.image.load(r'FADE\Fade_7.png'),
        pygame.image.load(r'FADE\Fade_6.png'),
        pygame.image.load(r'FADE\Fade_5.png'),
        pygame.image.load(r'FADE\Fade_4.png'),
        pygame.image.load(r'FADE\Fade_3.png'),
        pygame.image.load(r'FADE\Fade_2.png'),
        pygame.image.load(r'FADE\Fade_1.png')
]

    #커서 이미지
img_main_Cursor = pygame.image.load(r'MAIN\MAIN_CURSOR.png')
img_option_Cursor = pygame.image.load(r'CURSOR\CURSOR.png')
#출처 "https://www.flaticon.com/kr/free-icons/"

    #가이드 이미지
img_main_Guide = pygame.image.load(r'MAIN\MAIN_GUIDE.png')

    #곡 자켓 이미지
img_Song_jacket = [
                pygame.image.load(r'SONG_JACKET\Select_Song_img_August_Snowfall.png'), 
                pygame.image.load(r'SONG_JACKET\Select_Song_img_Avalanche.png'),
                pygame.image.load(r'SONG_JACKET\Select_Song_img_Ice_Dust.png')
                ]

img_Song_jacket_Size = img_Song_jacket[0].get_rect().size
img_Song_jacket_Horizon = img_Song_jacket_Size[0]
img_Song_jacket_Vertical = img_Song_jacket_Size[1]

    #랭크 이미지
img_Rank_P = pygame.image.load(r'RANK\RANK_P.png')
img_Rank_S = pygame.image.load(r'RANK\RANK_S.png')
img_Rank_A = pygame.image.load(r'RANK\RANK_A.png')
img_Rank_B = pygame.image.load(r'RANK\RANK_B.png')
img_Rank_C = pygame.image.load(r'RANK\RANK_C.png')
img_Rank_D = pygame.image.load(r'RANK\RANK_D.png')

img_Rank_Size = img_Rank_S.get_rect().size
img_Rank_Horizon = img_Rank_Size[0]
img_Rank_Vertical = img_Rank_Size[1]

    #결과창 이미지
img_Result_Result = pygame.image.load(r'RESULT\RESULT.png')
img_Result_Result_Size = img_Result_Result.get_size()
img_Result_Result_Horizon = img_Result_Result_Size[0]
img_Result_Result_Vertical = img_Result_Result_Size[1]

    # 폰트 정의
Combo_Font = pygame.font.Font(r'FONT\Danjo\Danjo_bold_Regular.otf', 70)
Back_Font = pygame.font.Font(r'FONT\Danjo\Danjo_bold_Regular.otf', 70)
Early_Late_Font = pygame.font.Font(r'FONT\Danjo\Danjo_bold_Regular.otf', 30)
UI_Font = pygame.font.Font(r'FONT\Danjo\Danjo_bold_Regular.otf', 20)
Ratio_Font = pygame.font.Font(r'FONT\Danjo\Danjo_bold_Regular.otf', 30)
Writer_Font = pygame.font.Font(r'FONT\Danjo\Danjo_bold_Regular.otf', 50)
#출처 https://noonnu.cc/font_page/1173


# 메인 선택옵션 사이즈 구하기
img_main_Title_Size = img_main_Title.get_rect().size
img_main_Title_Horizon = img_main_Title_Size[0]
img_main_Title_Vertical = img_main_Title_Size[1]

img_main_Start_Size = img_main_Start_ON.get_rect().size
img_main_Start_Horizon = img_main_Start_Size[0]
img_main_Start_Vertical = img_main_Start_Size[1]

img_main_Option_Size = img_main_Option_ON.get_rect().size
img_main_Option_Horizon = img_main_Start_Size[0]
img_main_Option_Vertical = img_main_Start_Size[1]

img_main_Exit_Size = img_main_Exit_ON.get_rect().size
img_main_Exit_Horizon = img_main_Exit_Size[0]
img_main_Exit_Vertical = img_main_Exit_Size[1]

#메인 가이드 사이즈 구하기
img_main_Guide_Size = img_main_Guide.get_rect().size
img_main_Guide_Horizon = img_main_Guide_Size[0]
img_main_Guide_Vertical = img_main_Guide_Size[1]

# 판정 이미지 사이즈 구하기
img_Judge_PGREAT_Size = img_Judge_PGREAT.get_rect().size
img_Judge_GREAT_Size = img_Judge_GREAT.get_rect().size
img_Judge_GOOD_Size = img_Judge_GOOD.get_rect().size
img_Judge_MISS_Size = img_Judge_MISS.get_rect().size

img_Judge_Vertical = img_Judge_PGREAT_Size[1]

img_Judge_PGREAT_Horizon = img_Judge_PGREAT_Size[0]
img_Judge_GREAT_Horizon = img_Judge_GREAT_Size[0]
img_Judge_GOOD_Horizon = img_Judge_GOOD_Size[0]
img_Judge_MISS_Horizon = img_Judge_MISS_Size[0]

# 노트 사이즈 구하기
img_Note_Press_Size = img_Note_Press.get_rect().size
img_Note_Press_Horizon = img_Note_Press_Size[0]
img_Note_Press_Vertical = img_Note_Press_Size[1]

# 노트 터치이미지 좌표 찍기
img_Note_Press_1_X_Pos = w/2 - w/10 - img_Note_Press_Horizon/2
img_Note_Press_1_Y_Pos = h/2 + h/5.625 - img_Note_Press_Vertical/2

img_Note_Press_2_X_Pos = w/2 - img_Note_Press_Horizon/2
img_Note_Press_2_Y_Pos = h/2 + h/5.625 - img_Note_Press_Vertical/2

img_Note_Press_3_X_Pos = w/2 + w/10 - img_Note_Press_Horizon/2
img_Note_Press_3_Y_Pos = h/2 + h/5.625 - img_Note_Press_Vertical/2

img_Note_Press_4_X_Pos = w/2 - w/10 - img_Note_Press_Horizon/2
img_Note_Press_4_Y_Pos = h/2 - img_Note_Press_Vertical/2

img_Note_Press_5_X_Pos = w/2 - img_Note_Press_Horizon/2
img_Note_Press_5_Y_Pos = h/2 - img_Note_Press_Vertical/2

img_Note_Press_6_X_Pos = w/2 + w/10 - img_Note_Press_Horizon/2
img_Note_Press_6_Y_Pos = h/2 - img_Note_Press_Vertical/2

img_Note_Press_7_X_Pos = w/2 - w/10 - img_Note_Press_Horizon/2
img_Note_Press_7_Y_Pos = h/2 - h/5.625 - img_Note_Press_Vertical/2

img_Note_Press_8_X_Pos = w/2 - img_Note_Press_Horizon/2
img_Note_Press_8_Y_Pos = h/2 - h/5.625 - img_Note_Press_Vertical/2

img_Note_Press_9_X_Pos = w/2 + w/10 - img_Note_Press_Horizon/2
img_Note_Press_9_Y_Pos = h/2 - h/5.625 - img_Note_Press_Vertical/2

# 키입력 감지
key_Press = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# 노트 속도
Note_Speed = 0.5

# 인게임 시스템
    #JUDGE
judge_array = [0, 0, 0, 0]
judge_100p = 50
judge_100 = 100
judge_50 = 150
judge_print = -1
judge_frame = 0
Total_Note = 0
Ratio = 0

combo = 0

Early_Late = -1

Option_Current_Page = 0
All_Page = 2 - 1
Change_Page = 0

    #OPTION
Note_Color = BLACK
Current_Note_Color = 8 - 1

Hit_Sound_Volume = 1
Effect_Volume = 1

Effect_Sound = pygame.mixer.Sound(r'Sound\Effect.mp3')
Select_Sound = pygame.mixer.Sound(r'Sound\Select.mp3')
Song_Start_Sound = pygame.mixer.Sound(r'Sound\Song_Start.mp3')

Hit_Sound_Array = [
            pygame.mixer.Sound(r'Sound\Hit_Sound_1.mp3'),
            pygame.mixer.Sound(r'Sound\Hit_Sound_2.mp3'),
            pygame.mixer.Sound(r'Sound\Hit_Sound_3.mp3')
            ]

Hit_Sound_Name = [
            'Stick',
            'Drum',
            'Clap'
            ]

Current_Hit_Sound = 0
All_Hit_Sound = 3 - 1

Hit_Sound = pygame.mixer.Sound(Hit_Sound_Array[Current_Hit_Sound])

    #COLOR

Color_Array = [RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, WHITE, BLACK]
Color_Array_Size = 8 - 1

    #JACKET
Current_jacket = 0
jacket_Size = 3 - 1
jacket_LEFT_Pos = (-img_Song_jacket_Horizon/2, h/2 + h/16 - img_Song_jacket_Vertical/2)
jacket_CENTER_Pos = (w/2 - img_Song_jacket_Horizon/2, h/2 - img_Song_jacket_Vertical/2)
jacket_RIGHT_Pos = (w - img_Song_jacket_Horizon/2, h/2 + h/16 - img_Song_jacket_Vertical/2)

jacket_Name = [
                'August Snowfall',
                'Avalanche',
                'Ice Dust'
            ]
Song_Writer = [
                'PLUM',
                'PLUM',
                'PLUM'
            ]
Song = [
        pygame.mixer.Sound(r'SONG\Song_August_Snowfall.mp3'),
        pygame.mixer.Sound(r'SONG\Song_Avalanche.mp3'),
        pygame.mixer.Sound(r'SONG\Song_Ice_Dust.mp3')
        ]

    #PLAYING NOW
AutoMode = 0
Current_Play_Song = ''
Reading_Next = 0
Note_fps = 0
BPM = 0
Writer = ''
Beat = 0
SongOffSet = 0
Song_Play_fps = 0
Max_Combo = 0

    #Timer
Time_Measure = time.time()
Playing_Game_Time = 0
Time = 0
Fade_Time = 0
Result_Entrance_Time = 0

Time1 = 0
Time2 = 0
Compile_Time = 0

t = 0
tst = Time

    #DUPLICATE_NOTE
t1 = []
t2 = []
t3 = []
t4 = []
t5 = []
t6 = []
t7 = []
t8 = []
t9 = []

def sum_Note(n):

    global Note_Speed

    ty = 0
    tst = Time + 1 - Note_Speed

    if n == 1:
        t1.append([t, tst])
    if n == 2:
        t2.append([t, tst])
    if n == 3:
        t3.append([t, tst])
    if n == 4:
        t4.append([t, tst])
    if n == 5:
        t5.append([t, tst])
    if n == 6:
        t6.append([t, tst])
    if n == 7:
        t7.append([t, tst])
    if n == 8:
        t8.append([t, tst])
    if n == 9:
        t9.append([t, tst])


    #PRINT_NOTE
Bar = 0

    #FADE
Fade_Bar = 0
Fade_Num = 0
Fade_Go = 0

Pattern = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] #Note 1 ~ 9, Only Check 10 ~ 11, Beat 12

#커서 세팅
Main_Cursor_Current = 'START'

Option_Cursor_Pos = (w - w/5, h/2 - h/4 - 15)
Option_Cursor_Current = 'NOTE_SPEED'

#이벤트 루프
IsRunning = True
Window = 'Main'
WindowPlay = 1

judge_print = -1

def judge(n):

    global combo
    global judge_print
    global Early_Late
    global Total_Note
    global Ratio

    if n >= 192 - (w/10 / Note_Speed * (judge_100p / 1000)) and n <= 192 + (w/10 / Note_Speed * (judge_100p / 1000)):
        judge_print = 0
        combo += 1
        Total_Note += 1
        judge_array[0] += 1
        Ratio = (judge_array[0] * 100 + judge_array[1] * 75 + judge_array[2] * 50) / Total_Note

    if n >= 192 - (w/10 / Note_Speed * (judge_100 / 1000)) and n < 192 - (w/10 / Note_Speed * (judge_100p / 1000)):
        judge_print = 1
        Early_Late = 1
        combo += 1
        Total_Note += 1
        judge_array[1] += 1
        Ratio = (judge_array[0] * 100 + judge_array[1] * 75 + judge_array[2] * 50) / Total_Note

    if n <= 192 + (w/10 / Note_Speed * (judge_100 / 1000)) and n > 192 + (w/10 / Note_Speed * (judge_100p / 1000)):
        judge_print = 1
        Early_Late = 0
        combo += 1
        Total_Note += 1
        judge_array[1] += 1
        Ratio = (judge_array[0] * 100 + judge_array[1] * 75 + judge_array[2] * 50) / Total_Note

    if n >= 192 - (w/10 / Note_Speed * (judge_50 / 1000)) and n < 192 - (w/10 / Note_Speed * (judge_100 / 1000)):
        judge_print = 2
        Early_Late = 1
        combo += 1
        Total_Note += 1
        judge_array[2] += 1
        Ratio = (judge_array[0] * 100 + judge_array[1] * 75 + judge_array[2] * 50) / Total_Note

    if n <= 192 + (w/10 / Note_Speed * (judge_50 / 1000)) and n > 192 + (w/10 / Note_Speed * (judge_100 / 1000)):
        judge_print = 2
        Early_Late = 0
        combo += 1
        Total_Note += 1
        judge_array[2] += 1
        Ratio = (judge_array[0] * 100 + judge_array[1] * 75 + judge_array[2] * 50) / Total_Note


while IsRunning:

    if WindowPlay == 0:

        Time = time.time() - Time_Measure

        #Fade
        if Time - Fade_Time > Fade_Bar:

            if Fade_Num >= 19:
                Fade_Bar = 0
                Fade_Num = 0
                WindowPlay = 1
                
            Fade_Bar += 0.05
            Screen.blit(Fade[Fade_Num], (0, 0))
            Fade_Num += 1
                
            #Check EVENT
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #QUIT GAME
                    IsRunning = False       
                            

    if Window == 'Main' and WindowPlay == 1:
        
        Time = time.time() - Time_Measure

        #Version
        View_Version = UI_Font.render(str(Version), True, WHITE)
        View_Version_Size = View_Version.get_size()
        View_Version_Horizon = View_Version_Size[0]
        View_Version_Vertical = View_Version_Size[1]

        #Set BG
        Screen.blit(img_Background_Main, (0, 0))
        Screen.blit(View_Version, (10, h - View_Version_Vertical - 10))

        if Main_Cursor_Current == 'START':
            Screen.blit(img_main_Start_ON, (w/2 - img_main_Option_Horizon - img_main_Option_Horizon/2 - img_main_Option_Horizon/4, h/2 - img_main_Option_Vertical/2.3))
            Screen.blit(img_main_Option_OFF, (w/2 - img_main_Option_Horizon/2, h/2 - img_main_Option_Vertical/2.3))
            Screen.blit(img_main_Exit_OFF, (w/2 + img_main_Option_Horizon/2 + img_main_Option_Horizon/4, h/2 - img_main_Option_Vertical/2.3))

        if Main_Cursor_Current == 'OPTION':
            Screen.blit(img_main_Start_OFF, (w/2 - img_main_Option_Horizon - img_main_Option_Horizon/2 - img_main_Option_Horizon/4, h/2 - img_main_Option_Vertical/2.3))
            Screen.blit(img_main_Option_ON, (w/2 - img_main_Option_Horizon/2, h/2 - img_main_Option_Vertical/2.3))
            Screen.blit(img_main_Exit_OFF, (w/2 + img_main_Option_Horizon/2 + img_main_Option_Horizon/4, h/2 - img_main_Option_Vertical/2.3))

        if Main_Cursor_Current == 'EXIT':
            Screen.blit(img_main_Start_OFF, (w/2 - img_main_Option_Horizon - img_main_Option_Horizon/2 - img_main_Option_Horizon/4, h/2 - img_main_Option_Vertical/2.3))
            Screen.blit(img_main_Option_OFF, (w/2 - img_main_Option_Horizon/2, h/2 - img_main_Option_Vertical/2.3))
            Screen.blit(img_main_Exit_ON, (w/2 + img_main_Option_Horizon/2 + img_main_Option_Horizon/4, h/2 - img_main_Option_Vertical/2.3))


        Screen.blit(img_main_Guide, (w/2 - img_main_Guide_Horizon/2, h - img_main_Guide_Vertical))
        Screen.blit(img_main_Title, (w/2 - img_main_Title_Horizon/2, img_main_Title_Vertical/100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #QUIT GAME
                IsRunning = False

            IsPressed_Arrow = 0

            #KEYDOWN
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    SoundChannel_EFFECT.play(Effect_Sound)

                    if Main_Cursor_Current == 'START' and IsPressed_Arrow == 0:
                        Main_Cursor_Current = 'OPTION'
                        IsPressed_Arrow = 1

                    if Main_Cursor_Current == 'OPTION' and IsPressed_Arrow == 0:
                        Main_Cursor_Current = 'EXIT'
                        IsPressed_Arrow = 1

                if event.key == pygame.K_LEFT:
                    SoundChannel_EFFECT.play(Effect_Sound)

                    if Main_Cursor_Current == 'EXIT' and IsPressed_Arrow == 0:
                        Main_Cursor_Current = 'OPTION'
                        IsPressed_Arrow = 1

                    if Main_Cursor_Current == 'OPTION' and IsPressed_Arrow == 0:
                        Main_Cursor_Current = 'START'
                        IsPressed_Arrow = 1

                if event.key == pygame.K_SPACE:
                    SoundChannel_SELECT.play(Select_Sound)

                    if Main_Cursor_Current == 'START':
                        Fade_Time = Time
                        WindowPlay = 0
                        Window = 'Select_Song'

                    if Main_Cursor_Current == 'OPTION':
                        Fade_Time = Time
                        WindowPlay = 0
                        Window = 'Option'

                    if Main_Cursor_Current == 'EXIT':
                        IsRunning = False

            #KEYUP
            if event.type == pygame.KEYUP:
                pass


    if Window == 'Option' and WindowPlay == 1:

        Time = time.time() - Time_Measure

        img_Option_Size = img_main_Option.get_size()

        #Font Render
        View_Page = Combo_Font.render(str("-- %d / %d --" %((Option_Current_Page+1), (All_Page+1))), True, BLACK)
        View_Page_Size = View_Page.get_size()
        View_Page_Horizon = View_Page_Size[0]
        View_Page_Vertical = View_Page_Size[1]
        
        #Set BG
        Screen.blit(img_Background_Option, (0, 0))

        Screen.blit(img_main_Option, (w/2 - img_Option_Size[0]/2, img_Option_Size[1]/8))
        Screen.blit(img_option_Cursor, Option_Cursor_Pos)
        Screen.blit(View_Page, (w/2 - View_Page_Horizon/2, h - View_Page_Vertical))

        if Option_Current_Page == 0:
            #Font Render
            Note_Speed_Font = Combo_Font.render(str("SPEED UP & DOWN 9 ~ 20  <- %d ->" %(25 - Note_Speed*20)), True, WHITE)
            Note_Frame_Font = Combo_Font.render(str("NOTE FRAME"), True, WHITE)
            Note_Color_Font = Combo_Font.render(str("NOTE COLOR"), True, Note_Color)

            #Font Write
            Screen.blit(Note_Speed_Font, (w/8, h/2 - h/4))
            Screen.blit(Note_Frame_Font, (w/8, (h - h/4 + h/6)/2))
            Screen.blit(Note_Color_Font, (w/8, h/2 + h/6))

            #Draw Note Frame / Color
            Note_Frame_Size = img_Note_Frame[Current_Note_Frame].get_size()
            Note_Frame_Horizon = Note_Frame_Size[0]
            Note_Frame_Vertical = Note_Frame_Size[1]
            Screen.blit(img_Note_Frame[Current_Note_Frame], (w/2 + Note_Frame_Horizon/2, (h - h/4 + h/6)/2 - Note_Frame_Vertical/2))

            pygame.draw.rect(Screen, Note_Color, (w/2 + w/20, h/2 + h/6 - h/11.25, w/10, h/5.625))

            if Change_Page == 1:
                Option_Cursor_Current = 'NOTE_SPEED'
                Option_Cursor_Pos = (w - w/5, h/2 - h/4 - 15)
                Change_Page = 0

        if Option_Current_Page == 1:
            #Font Render
            Hit_Sound_Font = Combo_Font.render(str("Hit Sound <- %s ->") %Hit_Sound_Name[Current_Hit_Sound], True, WHITE)
            Hit_Sound_Volume_Font = Combo_Font.render(str("Hit Sound Volume 0 ~ 10  <- %d ->" %(Hit_Sound_Volume * 10)), True, WHITE)
            Effect_Volume_Font = Combo_Font.render(str("Effect Volume 0 ~ 10  <- %d ->" %(Effect_Volume * 10)), True, WHITE)

            #Font Write
            Screen.blit(Hit_Sound_Font, (w/8, h/2 - h/4))
            Screen.blit(Hit_Sound_Volume_Font, (w/8, h/2 + h/6))
            Screen.blit(Effect_Volume_Font, (w/8, (h - h/4 + h/6)/2))

            if Change_Page == 1:
                Option_Cursor_Current = 'HIT_SOUND'
                Option_Cursor_Pos = (w - w/5, h/2 - h/4 - 15)
                Change_Page = 0


        for event in pygame.event.get():
            if event.type == pygame.QUIT: #QUIT GAME
                IsRunning = False
            
            IsPressed_Arrow = 0

            #KEYDOWN
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    SoundChannel_SELECT.play(Select_Sound)
                    Window = 'Main'
                    Fade_Time = Time
                    WindowPlay = 0
                
                if event.key == pygame.K_SPACE:
                    SoundChannel_SELECT.play(Select_Sound)
                    if Option_Current_Page >= All_Page:
                        Option_Current_Page = 0
                    else:
                        Option_Current_Page += 1
                    Change_Page = 1 
                    IsPressed_Arrow = 1

                if Option_Current_Page == 0:
                    if event.key == pygame.K_DOWN:

                        SoundChannel_EFFECT.play(Effect_Sound)

                        if Option_Cursor_Current == 'NOTE_SPEED' and IsPressed_Arrow == 0:
                            Option_Cursor_Pos = (w - w/5, (h - h/4 + h/6)/2 - 15)
                            Option_Cursor_Current = 'NOTE_FRAME'
                            IsPressed_Arrow = 1

                        if Option_Cursor_Current == 'NOTE_FRAME' and IsPressed_Arrow == 0:
                            Option_Cursor_Pos = (w - w/5, h/2 + h/6 - 15)
                            Option_Cursor_Current = 'NOTE_COLOR'
                            IsPressed_Arrow = 1
    
                    if event.key == pygame.K_UP:

                        SoundChannel_EFFECT.play(Effect_Sound)

                        if Option_Cursor_Current == 'NOTE_COLOR' and IsPressed_Arrow == 0:
                            Option_Cursor_Pos = (w - w/5, (h - h/4 + h/6)/2 - 15)
                            Option_Cursor_Current = 'NOTE_FRAME'
                            IsPressed_Arrow = 1

                        if Option_Cursor_Current == 'NOTE_FRAME' and IsPressed_Arrow == 0:
                            Option_Cursor_Pos = (w - w/5, h/2 - h/4 - 15)
                            Option_Cursor_Current = 'NOTE_SPEED'
                            IsPressed_Arrow = 1

                    if event.key == pygame.K_LEFT:

                        SoundChannel_EFFECT.play(Effect_Sound)

                        if Option_Cursor_Current == 'NOTE_SPEED' and IsPressed_Arrow == 0 and Note_Speed < 0.75:
                            Note_Speed += 0.05
                            IsPressed_Arrow = 1

                        if Option_Cursor_Current == 'NOTE_FRAME' and IsPressed_Arrow == 0:
                            if Current_Note_Frame <= 0:
                                Current_Note_Frame = Note_Frame_Array
                            else:
                                Current_Note_Frame -= 1
                            IsPressed_Arrow = 1

                        if Option_Cursor_Current == 'NOTE_COLOR' and IsPressed_Arrow == 0:
                            if Current_Note_Color <= 0:
                                Current_Note_Color = Color_Array_Size
                                Note_Color = Color_Array[Current_Note_Color]
                            else:
                                Current_Note_Color -= 1
                                Note_Color = Color_Array[Current_Note_Color]
                            IsPressed_Arrow = 1
                            
                    if event.key == pygame.K_RIGHT:

                        SoundChannel_EFFECT.play(Effect_Sound)

                        if Option_Cursor_Current == 'NOTE_SPEED' and IsPressed_Arrow == 0 and Note_Speed > 0.26:
                            Note_Speed -= 0.05
                            IsPressed_Arrow = 1
                                    
                        if Option_Cursor_Current == 'NOTE_FRAME' and IsPressed_Arrow == 0:
                            if Current_Note_Frame >= Note_Frame_Array:
                                Current_Note_Frame = 0
                            else:
                                Current_Note_Frame += 1
                            IsPressed_Arrow = 1

                        if Option_Cursor_Current == 'NOTE_COLOR' and IsPressed_Arrow == 0:
                            if Current_Note_Color >= Color_Array_Size:
                                Current_Note_Color = 0
                                Note_Color = Color_Array[Current_Note_Color]
                                IsPressed_Arrow = 1
                            else:
                                Current_Note_Color += 1
                                Note_Color = Color_Array[Current_Note_Color]
                                IsPressed_Arrow = 1

                if Option_Current_Page == 1:
                    if event.key == pygame.K_DOWN:

                        SoundChannel_EFFECT.play(Effect_Sound)

                        if Option_Cursor_Current == 'HIT_SOUND' and IsPressed_Arrow == 0:
                            Option_Cursor_Pos = (w - w/5, (h - h/4 + h/6)/2 - 15)
                            Option_Cursor_Current = 'EFFECT_VOLUME'
                            IsPressed_Arrow = 1

                        if Option_Cursor_Current == 'EFFECT_VOLUME' and IsPressed_Arrow == 0:
                            Option_Cursor_Pos = (w - w/5, h/2 + h/6 - 15)
                            Option_Cursor_Current = 'HIT_SOUND_VOLUME'
                            IsPressed_Arrow = 1
    
                    if event.key == pygame.K_UP:

                        SoundChannel_EFFECT.play(Effect_Sound)

                        if Option_Cursor_Current == 'HIT_SOUND_VOLUME' and IsPressed_Arrow == 0:
                            Option_Cursor_Pos = (w - w/5, (h - h/4 + h/6)/2 - 15)
                            Option_Cursor_Current = 'EFFECT_VOLUME'
                            IsPressed_Arrow = 1

                        if Option_Cursor_Current == 'EFFECT_VOLUME' and IsPressed_Arrow == 0:
                            Option_Cursor_Pos = (w - w/5, h/2 - h/4 - 15)
                            Option_Cursor_Current = 'HIT_SOUND'
                            IsPressed_Arrow = 1

                    if event.key == pygame.K_LEFT:

                        if Option_Cursor_Current == 'HIT_SOUND' and IsPressed_Arrow == 0:

                            if Current_Hit_Sound > 0:
                                Current_Hit_Sound -= 1
                                Hit_Sound = Hit_Sound_Array[Current_Hit_Sound]

                            IsPressed_Arrow = 1

                            SoundChannel_HITSOUND.play(Hit_Sound)

                        if Option_Cursor_Current == 'EFFECT_VOLUME' and IsPressed_Arrow == 0:

                            if Effect_Volume >= 0.1:
                                Effect_Volume -= 0.1
                                Effect_Sound.set_volume(Effect_Volume)
                                Select_Sound.set_volume(Effect_Volume)
                                Song_Start_Sound.set_volume(Effect_Volume)
                                IsPressed_Arrow = 1

                            SoundChannel_EFFECT.play(Effect_Sound)

                        if Option_Cursor_Current == 'HIT_SOUND_VOLUME' and IsPressed_Arrow == 0:

                            if Hit_Sound_Volume >= 0.1:
                                Hit_Sound_Volume -= 0.1
                                Hit_Sound.set_volume(Hit_Sound_Volume)
                                IsPressed_Arrow = 1

                            SoundChannel_HITSOUND.play(Hit_Sound)

                    if event.key == pygame.K_RIGHT:

                        if Option_Cursor_Current == 'HIT_SOUND' and IsPressed_Arrow == 0:

                            if Current_Hit_Sound < All_Hit_Sound:
                                Current_Hit_Sound += 1
                                Hit_Sound = Hit_Sound_Array[Current_Hit_Sound]

                            IsPressed_Arrow = 1

                            Hit_Sound.set_volume(Hit_Sound_Volume)
                            SoundChannel_HITSOUND.play(Hit_Sound)

                        if Option_Cursor_Current == 'EFFECT_VOLUME' and IsPressed_Arrow == 0:

                            if Effect_Volume <= 0.9:
                                Effect_Volume += 0.1
                                Effect_Sound.set_volume(Effect_Volume)
                                Select_Sound.set_volume(Effect_Volume)
                                Song_Start_Sound.set_volume(Effect_Volume)
                                IsPressed_Arrow = 1

                            SoundChannel_EFFECT.play(Effect_Sound)

                        if Option_Cursor_Current == 'HIT_SOUND_VOLUME' and IsPressed_Arrow == 0:

                            if Hit_Sound_Volume <= 0.9:
                                Hit_Sound_Volume += 0.1
                                Hit_Sound.set_volume(Hit_Sound_Volume)
                                IsPressed_Arrow = 1

                            SoundChannel_HITSOUND.play(Hit_Sound)



            if event.type == pygame.KEYUP:
                pass


    if Window == 'Select_Song' and WindowPlay == 1:
        
        Time = time.time() - Time_Measure
        global Start_Time

        #Set BG
        Screen.blit(img_Background_Main, (0, 0))

        #Draw Jacket
        Screen.blit(img_Song_jacket[Current_jacket],jacket_CENTER_Pos)
        if Current_jacket >= jacket_Size:
            Screen.blit(img_Song_jacket[Current_jacket-1], jacket_LEFT_Pos)
            Screen.blit(img_Song_jacket[0], jacket_RIGHT_Pos)
        elif Current_jacket <= 0:
            Screen.blit(img_Song_jacket[jacket_Size], jacket_LEFT_Pos)
            Screen.blit(img_Song_jacket[Current_jacket+1], jacket_RIGHT_Pos)
        else:
            Screen.blit(img_Song_jacket[Current_jacket-1], jacket_LEFT_Pos)
            Screen.blit(img_Song_jacket[Current_jacket+1], jacket_RIGHT_Pos)
        
        #Set Font
        Font_Song_Select = Combo_Font.render(str("SELECT SONG"), True, WHITE)
        Font_Song_Name = Combo_Font.render(str("%s" %jacket_Name[Current_jacket]), True, WHITE)
        Font_Song_Writer = Writer_Font.render(str(Song_Writer[Current_jacket]), True, WHITE)

        #Get Song Name Font Size
        Font_Song_Name_Size = Font_Song_Name.get_size()
        Font_Song_Name_Horizon = Font_Song_Name_Size[0]
        Font_Song_Name_Vertical = Font_Song_Name_Size[1]
        
        Font_Song_Select_Size = Font_Song_Select.get_size()
        Font_Song_Select_Horizon = Font_Song_Select_Size[0]
        Font_Song_Select_Vertical = Font_Song_Select_Size[1]

        Font_Song_Writer_Size = Font_Song_Writer.get_size()
        Font_Song_Writer_Horizon = Font_Song_Writer_Size[0]
        Font_Song_Writer_Vertical = Font_Song_Writer_Size[1]

        #Write Font
        Screen.blit(Font_Song_Select, (w/2 - Font_Song_Select_Horizon/2, Font_Song_Select_Vertical/2))
        Screen.blit(Font_Song_Writer, (w/2 - Font_Song_Writer_Horizon/2, Font_Song_Select_Vertical * 2))
        Screen.blit(Font_Song_Name, (w/2 - Font_Song_Name_Horizon/2, h/2 + h/4 - Font_Song_Name_Vertical/8))


        for event in pygame.event.get():
            if event.type == pygame.QUIT: #QUIT GAME
                IsRunning = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    SoundChannel_SELECT.play(Select_Sound)
                    Fade_Time = Time
                    WindowPlay = 0
                    Window = 'Main'

                if event.key == pygame.K_LEFT:

                    SoundChannel_EFFECT.play(Effect_Sound)

                    if Current_jacket <= 0:
                        Current_jacket = jacket_Size
                    else:
                        Current_jacket -= 1

                if event.key == pygame.K_RIGHT:
                    
                    SoundChannel_EFFECT.play(Effect_Sound)

                    if Current_jacket >= jacket_Size:
                        Current_jacket = 0
                    else:
                        Current_jacket += 1
                
                if event.key == pygame.K_SPACE:

                    SoundChannel_SONGSELECT.play(Song_Start_Sound)
                    Current_Play_Song = jacket_Name[Current_jacket]
                    PlaySong = 0

                    #Reset Note Array
                    t1 = []
                    t2 = []
                    t3 = []
                    t4 = []
                    t5 = []
                    t6 = []
                    t7 = []
                    t8 = []
                    t9 = []

                    #Reset Ratio
                    for i in range(4):
                        judge_array[i] = 0
                    
                    Total_Note = 0
                    Ratio = 0

                    if Current_jacket == 0:
                        Current_Play_Song_Pattern = open(r'PATTERN\August_Snowfall.txt', 'r')

                    if Current_jacket == 1:
                        Current_Play_Song_Pattern = open(r'PATTERN\Avalanche.txt', 'r')

                    if Current_jacket == 2:
                        Current_Play_Song_Pattern = open(r'PATTERN\Ice_Dust.txt', 'r')

                    Current_Play_Song_Pattern.seek(0)
                    Current_Play_Song = Current_Play_Song_Pattern.readline()
                    Writer = str(Current_Play_Song_Pattern.readline())
                    SongOffSet = float(Current_Play_Song_Pattern.readline())
                    BPM = float(Current_Play_Song_Pattern.readline())
                    Time = time.time() - Time_Measure
                    Fade_Time = Time
                    Start_Time = Time

                    Window = 'InGame'
                    WindowPlay = 0
                        
            
            if event.type == pygame.KEYUP:
                pass


    if Window == 'InGame' and WindowPlay == 1:

        Compile_Time = Time2 - Time1
        Time = time.time() - Time_Measure
        Time1 = time.time() - Time_Measure

        if combo > Max_Combo:
            Max_Combo = combo

        #AutoMode ON
        if AutoMode == 1:

            if len(t1) > 0:
                if t1[0][0] >= 192:
                    judge(t1[0][0])
                    del t1[0]
                    SoundChannel_HITSOUND.play(Hit_Sound)
            if len(t2) > 0:
                if t2[0][0] >= 192:
                    judge(t2[0][0])
                    del t2[0]
                    SoundChannel_HITSOUND.play(Hit_Sound)
            if len(t3) > 0:
                if t3[0][0] >= 192:
                    judge(t3[0][0])
                    del t3[0]
                    SoundChannel_HITSOUND.play(Hit_Sound)
            if len(t4) > 0:
                if t4[0][0] >= 192:
                    judge(t4[0][0])
                    del t4[0]
                    SoundChannel_HITSOUND.play(Hit_Sound)
            if len(t5) > 0:
                if t5[0][0] >= 192:
                    judge(t5[0][0])
                    del t5[0]
                    SoundChannel_HITSOUND.play(Hit_Sound)
            if len(t6) > 0:
                if t6[0][0] >= 192:
                    judge(t6[0][0])
                    del t6[0]
                    SoundChannel_HITSOUND.play(Hit_Sound)
            if len(t7) > 0:
                if t7[0][0] >= 192:
                    judge(t7[0][0])
                    del t7[0]
                    SoundChannel_HITSOUND.play(Hit_Sound)
            if len(t8) > 0:
                if t8[0][0] >= 192:
                    judge(t8[0][0])
                    del t8[0]
                    SoundChannel_HITSOUND.play(Hit_Sound)
            if len(t9) > 0:
                if t9[0][0] >= 192:
                    judge(t9[0][0])
                    del t9[0]
                    SoundChannel_HITSOUND.play(Hit_Sound)

        #When Play Song
        if PlaySong == 0:
            if  Time - Start_Time >= SongOffSet / 1000: 
                SoundChannel_BGM.play(Song[Current_jacket])
                PlaySong = 1


        #Read File / Spawn Note
        if Time - Start_Time >= Bar: 
            for i in range(11):
                Pattern[i] = float(Current_Play_Song_Pattern.read(1))
                dummy = Current_Play_Song_Pattern.read(1)

                if Pattern[i] == 1:
                    sum_Note(i+1)

            Pattern[11] = float(Current_Play_Song_Pattern.readline())

            if Pattern[11] != 0:
                Bar += 1 / (((BPM / 60) * Pattern[11]) / 4) - Compile_Time/Pattern[11]
                print(Time1, Time2, Compile_Time, 1 / (((BPM / 60) * Pattern[11]) / 4) - Compile_Time/Pattern[11])

        #Conclude File / InGame
        if Pattern[11] == 0: 
            Song[Current_jacket].stop()
            Current_Play_Song_Pattern.close()
            Writer = 0
            SongOffSet = 0
            BPM = 0
            PlaySong = 0
            Note_fps = 0
            Pattern = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
            combo = 0
            Bar = 0
            Window = 'Result'
            Fade_Time = Time
            WindowPlay = 0

        #Set BG
        Screen.blit(img_Background_Main, (0, 0))
        pygame.draw.rect(Screen, (128,128,128), (w/2 - w/4 + w/16, 0, w/2 - w/8, h), 0)
        pygame.draw.rect(Screen, (211,211,211), (w/2 - w/4 + w/16, 0, w/2 - w/8, h), 10)

        #Draw AutoMode ON/OFF
        if AutoMode == 1:
            AutoMode_ONOFF = UI_Font.render(str("AutoMode ON (TAB)"), True, WHITE)
        elif AutoMode == 0:
            AutoMode_ONOFF = UI_Font.render(str("AutoMode OFF (TAB)"), True, BLACK)

        AutoMode_ONOFF_Size = AutoMode_ONOFF.get_size()
        AutoMode_ONOFF_Horizon = AutoMode_ONOFF_Size[0]
        AutoMode_ONOFF_Vertical = AutoMode_ONOFF_Size[1]

        Screen.blit(AutoMode_ONOFF, (w - AutoMode_ONOFF_Horizon, AutoMode_ONOFF_Vertical))

        #Draw Ratio
        View_Ratio = Ratio_Font.render(str("ACC : %.2f") %Ratio, True, BLACK)
        View_Ratio_Size = View_Ratio.get_size()
        View_Ratio_Horizon = View_Ratio_Size[0]
        View_Ratio_Vertical = View_Ratio_Size[1]

        Screen.blit(View_Ratio, (w/2 - View_Ratio_Horizon/2, h - h/16))

        #Draw Combo
        View_Combo = Combo_Font.render(str(combo), True, WHITE)
        View_Combo_Size = View_Combo.get_size()
        View_Combo_Horizon = View_Combo_Size[0]

        Screen.blit(View_Combo, (w/2 - View_Combo_Horizon/2, h - h/6))
        Note_Frame_Color = 0

        Note_Frame_Size = img_Note_Frame[Current_Note_Frame].get_size()
        Note_Frame_Horizon = Note_Frame_Size[0]
        Note_Frame_Vertical = Note_Frame_Size[1]

        #Draw Note Frame
        Screen.blit(img_Note_Frame[Current_Note_Frame], (w/2 - Note_Frame_Horizon - Note_Frame_Horizon/2, h/2 - Note_Frame_Vertical - Note_Frame_Vertical/2)) #1
        Screen.blit(img_Note_Frame[Current_Note_Frame], (w/2 - Note_Frame_Horizon/2, h/2  - Note_Frame_Vertical - Note_Frame_Vertical/2)) #2
        Screen.blit(img_Note_Frame[Current_Note_Frame], (w/2 + Note_Frame_Horizon/2, h/2  - Note_Frame_Vertical - Note_Frame_Vertical/2)) #3
        Screen.blit(img_Note_Frame[Current_Note_Frame], (w/2 - Note_Frame_Horizon - Note_Frame_Horizon/2, h/2 - Note_Frame_Vertical/2)) #4
        Screen.blit(img_Note_Frame[Current_Note_Frame], (w/2 - Note_Frame_Horizon/2, h/2  - Note_Frame_Vertical/2)) #5
        Screen.blit(img_Note_Frame[Current_Note_Frame], (w/2 + Note_Frame_Horizon/2, h/2  - Note_Frame_Vertical/2)) #6
        Screen.blit(img_Note_Frame[Current_Note_Frame], (w/2 - Note_Frame_Horizon - Note_Frame_Horizon/2, h/2 + Note_Frame_Vertical/2)) #7
        Screen.blit(img_Note_Frame[Current_Note_Frame], (w/2 - Note_Frame_Horizon/2, h/2  + Note_Frame_Vertical/2)) #8
        Screen.blit(img_Note_Frame[Current_Note_Frame], (w/2 + Note_Frame_Horizon/2, h/2  + Note_Frame_Vertical/2)) #9

        #Draw Side Line
        pygame.draw.line(Screen, CYAN, [w/2 - w/3, 0], [w/2 - w/3, h], 10)
        pygame.draw.line(Screen, MAGENTA, [w/2 + w/3, 0], [w/2 + w/3, h], 10)

        #Draw Note Press
        if key_Press[0] == 1:
            Screen.blit(img_Note_Press, (img_Note_Press_1_X_Pos, img_Note_Press_1_Y_Pos))
        if key_Press[1] == 1:
            Screen.blit(img_Note_Press, (img_Note_Press_2_X_Pos, img_Note_Press_2_Y_Pos))
        if key_Press[2] == 1:
            Screen.blit(img_Note_Press, (img_Note_Press_3_X_Pos, img_Note_Press_3_Y_Pos))
        if key_Press[3] == 1:
            Screen.blit(img_Note_Press, (img_Note_Press_4_X_Pos, img_Note_Press_4_Y_Pos))
        if key_Press[4] == 1:
            Screen.blit(img_Note_Press, (img_Note_Press_5_X_Pos, img_Note_Press_5_Y_Pos))
        if key_Press[5] == 1:
            Screen.blit(img_Note_Press, (img_Note_Press_6_X_Pos, img_Note_Press_6_Y_Pos))
        if key_Press[6] == 1:
            Screen.blit(img_Note_Press, (img_Note_Press_7_X_Pos, img_Note_Press_7_Y_Pos))
        if key_Press[7] == 1:
            Screen.blit(img_Note_Press, (img_Note_Press_8_X_Pos, img_Note_Press_8_Y_Pos))
        if key_Press[8] == 1:
            Screen.blit(img_Note_Press, (img_Note_Press_9_X_Pos, img_Note_Press_9_Y_Pos))

        #Draw Judge
        if judge_print == 0:
            Screen.blit(img_Judge_PGREAT, (w/2 - img_Judge_PGREAT_Horizon/2 , img_Judge_Vertical/2))

        if judge_print == 1:
            Screen.blit(img_Judge_GREAT, (w/2 - img_Judge_GREAT_Horizon/2 , img_Judge_Vertical/2))
            
            if Early_Late == 0:
                Font_Early_Late = Early_Late_Font.render(str("LATE"), True, MAGENTA)
                Screen.blit(Font_Early_Late, (w/2 + img_Judge_PGREAT_Horizon, img_Judge_Vertical/2 + h/32))

            elif Early_Late == 1:
                Font_Early_Late = Early_Late_Font.render(str("EARLY"), True, CYAN)
                Screen.blit(Font_Early_Late, (w/2 - img_Judge_PGREAT_Horizon - w/20, img_Judge_Vertical/2 + h/32))

        if judge_print == 2:
            Screen.blit(img_Judge_GOOD, (w/2 - img_Judge_GOOD_Horizon/2 , img_Judge_Vertical/2))
            
            if Early_Late == 0:
                Font_Early_Late = Early_Late_Font.render(str("LATE"), True, MAGENTA)
                Screen.blit(Font_Early_Late, (w/2 + img_Judge_PGREAT_Horizon, img_Judge_Vertical/2 + h/32))

            elif Early_Late == 1:
                Font_Early_Late = Early_Late_Font.render(str("EARLY"), True, CYAN)
                Screen.blit(Font_Early_Late, (w/2 - img_Judge_PGREAT_Horizon - w/20, img_Judge_Vertical/2 + h/32))

        if judge_print == 3:
            Screen.blit(img_Judge_MISS, (w/2 - img_Judge_MISS_Horizon/2 , img_Judge_Vertical/2))


        #Draw Note

        for tile_data in t1:
            
            tile_data[0] = (Time - tile_data[1]) * 350 / (Note_Speed * 2)
            
            if tile_data[0] <= 192:
                pygame.draw.rect(Screen, Note_Color, ((w/2 - w/10 - tile_data[0]/2, h/2 + h/5.625 - tile_data[0]/2, tile_data[0], tile_data[0])))
            else:
                pygame.draw.rect(Screen, Note_Color, (w/2 - w/10 - w/20, h/2 + h/5.625 - h/11.25, w/10, h/5.625))

            if tile_data[0] > 192 + (w/10 / Note_Speed * (judge_50 / 1000)):
                t1.remove(tile_data)
                judge_print = 3
                judge_array[3] += 1
                Total_Note += 1
                combo = 0
                Ratio = (judge_array[0] * 100 + judge_array[1] * 75 + judge_array[2] * 50) / Total_Note

        for tile_data in t2:
            
            tile_data[0] = (Time - tile_data[1]) * 350 / (Note_Speed * 2)
            
            if tile_data[0] <= 192:
                pygame.draw.rect(Screen, Note_Color, ((w/2 - tile_data[0]/2, h/2 + h/5.625 - tile_data[0]/2, tile_data[0], tile_data[0])))
            else:
                pygame.draw.rect(Screen, Note_Color, (w/2 - w/20, h/2 + h/5.625 - h/11.25, w/10, h/5.625))

            if tile_data[0] > 192 + (w/10 / Note_Speed * (judge_50 / 1000)):
                t2.remove(tile_data)
                judge_print = 3
                judge_array[3] += 1
                Total_Note += 1
                combo = 0
                Ratio = (judge_array[0] * 100 + judge_array[1] * 75 + judge_array[2] * 50) / Total_Note
                
        for tile_data in t3:
            
            tile_data[0] = (Time - tile_data[1]) * 350 / (Note_Speed * 2)
            
            if tile_data[0] <= 192:
                pygame.draw.rect(Screen, Note_Color, ((w/2 + w/10 - tile_data[0]/2, h/2 + h/5.625 - tile_data[0]/2, tile_data[0], tile_data[0])))
            else:
                pygame.draw.rect(Screen, Note_Color, (w/2 + w/10 - w/20, h/2 + h/5.625 - h/11.25, w/10, h/5.625))

            if tile_data[0] > 192 + (w/10 / Note_Speed * (judge_50 / 1000)):
                t3.remove(tile_data)
                judge_print = 3
                judge_array[3] += 1
                Total_Note += 1
                combo = 0
                Ratio = (judge_array[0] * 100 + judge_array[1] * 75 + judge_array[2] * 50) / Total_Note
                
        for tile_data in t4:
            
            tile_data[0] = (Time - tile_data[1]) * 350 / (Note_Speed * 2)
            
            if tile_data[0] <= 192:
                pygame.draw.rect(Screen, Note_Color, ((w/2 - w/10 - tile_data[0]/2, h/2 - tile_data[0]/2, tile_data[0], tile_data[0])))
            else:
                pygame.draw.rect(Screen, Note_Color, (w/2 - w/10 - w/20, h/2 - h/11.25, w/10, h/5.625))

            if tile_data[0] > 192 + (w/10 / Note_Speed * (judge_50 / 1000)):
                t4.remove(tile_data)
                judge_print = 3
                judge_array[3] += 1
                Total_Note += 1
                combo = 0
                Ratio = (judge_array[0] * 100 + judge_array[1] * 75 + judge_array[2] * 50) / Total_Note
                
        for tile_data in t5:
            
            tile_data[0] = (Time - tile_data[1]) * 350 / (Note_Speed * 2)
            
            if tile_data[0] <= 192:
                pygame.draw.rect(Screen, Note_Color, ((w/2 - tile_data[0]/2, h/2 - tile_data[0]/2, tile_data[0], tile_data[0])))
            else:
                pygame.draw.rect(Screen, Note_Color, (w/2 - w/20, h/2 - h/11.25, w/10, h/5.625))

            if tile_data[0] > 192 + (w/10 / Note_Speed * (judge_50 / 1000)):
                t5.remove(tile_data)
                judge_print = 3
                judge_array[3] += 1
                Total_Note += 1
                combo = 0
                Ratio = (judge_array[0] * 100 + judge_array[1] * 75 + judge_array[2] * 50) / Total_Note

        for tile_data in t6:
            
            tile_data[0] = (Time - tile_data[1]) * 350 / (Note_Speed * 2)
            
            if tile_data[0] <= 192:
                pygame.draw.rect(Screen, Note_Color, ((w/2 + w/10 - tile_data[0]/2, h/2 - tile_data[0]/2, tile_data[0], tile_data[0])))
            else:
                pygame.draw.rect(Screen, Note_Color, (w/2 + w/10 - w/20, h/2 - h/11.25, w/10, h/5.625))

            if tile_data[0] > 192 + (w/10 / Note_Speed * (judge_50 / 1000)):
                t6.remove(tile_data)
                judge_print = 3
                judge_array[3] += 1
                Total_Note += 1
                combo = 0
                Ratio = (judge_array[0] * 100 + judge_array[1] * 75 + judge_array[2] * 50) / Total_Note
                
        for tile_data in t7:
            
            tile_data[0] = (Time - tile_data[1]) * 350 / (Note_Speed * 2)
            
            if tile_data[0] <= 192:
                pygame.draw.rect(Screen, Note_Color, ((w/2 - w/10 - tile_data[0]/2, h/2 - h/5.625 - tile_data[0]/2, tile_data[0], tile_data[0])))
            else:
                pygame.draw.rect(Screen, Note_Color, (w/2 - w/10 - w/20, h/2 - h/5.625 - h/11.25, w/10, h/5.625))

            if tile_data[0] > 192 + (w/10 / Note_Speed * (judge_50 / 1000)):
                t7.remove(tile_data)
                judge_print = 3
                judge_array[3] += 1
                Total_Note += 1
                combo = 0
                Ratio = (judge_array[0] * 100 + judge_array[1] * 75 + judge_array[2] * 50) / Total_Note
                
        for tile_data in t8:
            
            tile_data[0] = (Time - tile_data[1]) * 350 / (Note_Speed * 2)
            
            if tile_data[0] <= 192:
                pygame.draw.rect(Screen, Note_Color, ((w/2 - tile_data[0]/2, h/2 - h/5.625 - tile_data[0]/2, tile_data[0], tile_data[0])))
            else:
                pygame.draw.rect(Screen, Note_Color, (w/2 - w/20, h/2 - h/5.625 - h/11.25, w/10, h/5.625))

            if tile_data[0] > 192 + (w/10 / Note_Speed * (judge_50 / 1000)):
                t8.remove(tile_data)
                judge_print = 3
                judge_array[3] += 1
                Total_Note += 1
                combo = 0
                Ratio = (judge_array[0] * 100 + judge_array[1] * 75 + judge_array[2] * 50) / Total_Note
                
        for tile_data in t9:
            
            tile_data[0] = (Time - tile_data[1]) * 350 / (Note_Speed * 2)
            
            if tile_data[0] <= 192:
                pygame.draw.rect(Screen, Note_Color, ((w/2 + w/10 - tile_data[0]/2, h/2 - h/5.625 - tile_data[0]/2, tile_data[0], tile_data[0])))
            else:
                pygame.draw.rect(Screen, Note_Color, (w/2 + w/10 - w/20, h/2 - h/5.625 - h/11.25, w/10, h/5.625))

            if tile_data[0] > 192 + (w/10 / Note_Speed * (judge_50 / 1000)):
                t9.remove(tile_data)
                judge_print = 3
                judge_array[3] += 1
                Total_Note += 1
                combo = 0
                Ratio = (judge_array[0] * 100 + judge_array[1] * 75 + judge_array[2] * 50) / Total_Note


        #Check EVENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #QUIT GAME
                IsRunning = False
            
            #KEYDOWN

            if event.type == pygame.KEYDOWN:
                
                #AutoMode ON/OFF
                if event.key == pygame.K_TAB:
                    if AutoMode == 1:
                        print("AutoMode OFF")
                        AutoMode = 0
                    elif AutoMode == 0:
                        AutoMode = 1
                        print("AutoMode ON")


                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    SoundChannel_HITSOUND.play(Hit_Sound)
                    key_Press[0] = 1
                    if len(t1) > 0:
                        if t1[0][0] >= 192 - (w/10 / Note_Speed * (judge_50 / 1000)):
                            judge(t1[0][0])
                            del t1[0]
                        
                if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    SoundChannel_HITSOUND.play(Hit_Sound)
                    key_Press[1] = 1
                    if len(t2) > 0:
                        if t2[0][0] > 192 - (w/10 / Note_Speed * (judge_50 / 1000)):
                            judge(t2[0][0])
                            del t2[0]

                if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    SoundChannel_HITSOUND.play(Hit_Sound)
                    key_Press[2] = 1
                    if len(t3) > 0:
                        if t3[0][0] > 192 - (w/10 / Note_Speed * (judge_50 / 1000)):
                            judge(t3[0][0])
                            del t3[0]

                if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    SoundChannel_HITSOUND.play(Hit_Sound)
                    key_Press[3] = 1
                    if len(t4) > 0:
                        if t4[0][0] > 192 - (w/10 / Note_Speed * (judge_50 / 1000)):
                            judge(t4[0][0])
                            del t4[0]

                if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    SoundChannel_HITSOUND.play(Hit_Sound)
                    key_Press[4] = 1
                    if len(t5) > 0:
                        if t5[0][0] > 192 - (w/10 / Note_Speed * (judge_50 / 1000)):
                            judge(t5[0][0])
                            del t5[0]

                if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    SoundChannel_HITSOUND.play(Hit_Sound)
                    key_Press[5] = 1
                    if len(t6) > 0:
                        if t6[0][0] > 192 - (w/10 / Note_Speed * (judge_50 / 1000)):
                            judge(t6[0][0])
                            del t6[0]

                if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    SoundChannel_HITSOUND.play(Hit_Sound)
                    key_Press[6] = 1
                    if len(t7) > 0:
                        if t7[0][0] > 192 - (w/10 / Note_Speed * (judge_50 / 1000)):
                            judge(t7[0][0])
                            del t7[0]

                if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    SoundChannel_HITSOUND.play(Hit_Sound)
                    key_Press[7] = 1
                    if len(t8) > 0:
                        if t8[0][0] > 192 - (w/10 / Note_Speed * (judge_50 / 1000)):
                            judge(t8[0][0])
                            del t8[0]

                if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    SoundChannel_HITSOUND.play(Hit_Sound)
                    key_Press[8] = 1
                    if len(t9) > 0:
                        if t9[0][0] > 192 - (w/10 / Note_Speed * (judge_50 / 1000)):
                            judge(t9[0][0])
                            del t9[0]

                #ESCAPE
                if event.key == pygame.K_ESCAPE:
                    Song[Current_jacket].stop()
                    Current_Play_Song_Pattern.close()
                    Writer = 0
                    SongOffSet = 0
                    BPM = 0
                    PlaySong = 0
                    Note_fps = 0
                    Pattern = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
                    combo = 0
                    Bar = 0
                    Window = 'Select_Song'
                    Fade_Time = Time
                    WindowPlay = 0

            #KEYUP  
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    key_Press[0] = 0
                if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    key_Press[1] = 0
                if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    key_Press[2] = 0
                if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    key_Press[3] = 0
                if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    key_Press[4] = 0
                if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    key_Press[5] = 0
                if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    key_Press[6] = 0
                if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    key_Press[7] = 0
                if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    key_Press[8] = 0
                    
        Time2 = time.time() - Time_Measure


    if Window == 'Result' and WindowPlay == 1:

        #Set BG
        Screen.blit(img_Background_Main, (0, 0))
        Screen.blit(img_Result_Result, (w/2 - img_Result_Result_Horizon/2, img_Result_Result_Vertical/3))
        Screen.blit(img_Song_jacket[Current_jacket], (w - w/16 - img_Song_jacket_Horizon, h/2 - img_Song_jacket_Vertical/2))
        Screen.blit(Font_Song_Name, (w - w/16 - Font_Song_Name_Horizon, h/2 + h/4 - Font_Song_Name_Vertical/8))

        #Draw Ratio
        View_Ratio = Combo_Font.render(str("ACC : %.2f") %Ratio, True, WHITE)
        View_Ratio_Size = View_Ratio.get_size()
        View_Ratio_Horizon = View_Ratio_Size[0]
        View_Ratio_Vertical = View_Ratio_Size[1]

        Screen.blit(View_Ratio, (w/20, img_Result_Result_Vertical/3))
        
        #Draw MaxCombo
        View_Combo = Ratio_Font.render(str("MAXCOMBO : %d" %Max_Combo), True, WHITE)
        View_Combo_Size = View_Combo.get_size()
        View_Combo_Horizon = View_Combo_Size[0]

        Screen.blit(View_Combo, (w/20, img_Result_Result_Vertical))

        Screen.blit(img_Judge_PGREAT, (w/10 - img_Judge_PGREAT_Horizon/2, h/4 - h/16 + img_Judge_PGREAT_Size[1]))
        Screen.blit(img_Judge_GREAT, (w/10 - img_Judge_GREAT_Horizon/2, h/4 - h/16 + img_Judge_PGREAT_Size[1]*2))
        Screen.blit(img_Judge_GOOD, (w/10 - img_Judge_GOOD_Horizon/2, h/4 - h/16 + img_Judge_PGREAT_Size[1]*3))
        Screen.blit(img_Judge_MISS, (w/10 - img_Judge_MISS_Horizon/2, h/4 - h/16 + img_Judge_PGREAT_Size[1]*4))

        PGREAT_Count = Combo_Font.render(str(judge_array[0]), True, WHITE)
        GREAT_Count = Combo_Font.render(str(judge_array[1]), True, WHITE)
        GOOD_Count = Combo_Font.render(str(judge_array[2]), True, WHITE)
        MISS_Count = Combo_Font.render(str(judge_array[3]), True, WHITE)

        Screen.blit(PGREAT_Count, (img_Judge_GREAT_Horizon*2, h/4 - h/16 + img_Judge_PGREAT_Size[1] + 25))
        Screen.blit(GREAT_Count, (img_Judge_GREAT_Horizon*2, h/4 - h/16 + img_Judge_PGREAT_Size[1]*2 + 25))
        Screen.blit(GOOD_Count, (img_Judge_GREAT_Horizon*2, h/4 - h/16 + img_Judge_PGREAT_Size[1]*3 + 25))
        Screen.blit(MISS_Count, (img_Judge_GREAT_Horizon*2, h/4 - h/16 + img_Judge_PGREAT_Size[1]*4 + 25))

        if Ratio >= 100:
            Screen.blit(img_Rank_P, (w/2 - img_Rank_Horizon/2, h/2 - img_Rank_Vertical/2))
        elif Ratio >= 95:
            Screen.blit(img_Rank_S, (w/2 - img_Rank_Horizon/2, h/2 - img_Rank_Vertical/2))
        elif Ratio >= 90:
            Screen.blit(img_Rank_A, (w/2 - img_Rank_Horizon/2, h/2 - img_Rank_Vertical/2))
        elif Ratio >= 85:
            Screen.blit(img_Rank_B, (w/2 - img_Rank_Horizon/2, h/2 - img_Rank_Vertical/2))
        elif Ratio >= 80:
            Screen.blit(img_Rank_C, (w/2 - img_Rank_Horizon/2, h/2 - img_Rank_Vertical/2))
        else:
            Screen.blit(img_Rank_D, (w/2 - img_Rank_Horizon/2, h/2 - img_Rank_Vertical/2))

        #Check EVENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #QUIT GAME
                IsRunning = False
            
            #KEYDOWN

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    SoundChannel_SELECT.play(Select_Sound)
                    Window = 'Select_Song'
                    Fade_Time = Time
                    WindowPlay = 0


    # Update Screen
    pygame.display.flip()


pygame.quit()