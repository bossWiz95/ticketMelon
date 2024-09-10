
class ticket:
    def __init__(self, url, openSeat_V, openSeat_R, openSeat_S, openSeat_A, openSeat_B, zoneCount_V, zoneCount_R, zoneCount_S, zoneCount_A, zoneCount_B,  zoneSelect_R1, zoneSelect_R2,
                 zoneSelect_V1, zoneSelect_V2, zoneSelect_S1, zoneSelect_S2, zoneSelect_A1, zoneSelect_A2, zoneSelect_B1, zoneSelect_B2, resetSeat, imgName, seatConfirm
                 , ticketCnt, ticketConfirm, pay_num1, pay_num2, pay_num3, pay_type, pay_bank, pay_tax, pay_agree, pay_confirm):
        self.url = url
        self.openSeat_V = openSeat_V
        self.openSeat_R = openSeat_R
        self.openSeat_S = openSeat_S
        self.openSeat_A = openSeat_A
        self.openSeat_B = openSeat_B
        self.zoneCount_V = zoneCount_V
        self.zoneCount_R = zoneCount_R
        self.zoneCount_S = zoneCount_S
        self.zoneCount_A = zoneCount_A
        self.zoneCount_B = zoneCount_B
        self.zoneSelect_V1 = zoneSelect_V1
        self.zoneSelect_V2 = zoneSelect_V2
        self.zoneSelect_R1 = zoneSelect_R1
        self.zoneSelect_R2 = zoneSelect_R2
        self.zoneSelect_S1 = zoneSelect_S1
        self.zoneSelect_S2 = zoneSelect_S2
        self.zoneSelect_A1 = zoneSelect_A1
        self.zoneSelect_A2 = zoneSelect_A2
        self.zoneSelect_B1 = zoneSelect_B1
        self.zoneSelect_B2 = zoneSelect_B2
        self.resetSeat = resetSeat
        self.imgName = imgName
        self.seatConfirm = seatConfirm
        self.ticketCnt = ticketCnt
        self.ticketConfirm = ticketConfirm
        self.pay_num1 = pay_num1
        self.pay_num2 = pay_num2
        self.pay_num3 = pay_num3
        self.pay_type = pay_num3
        self.pay_bank = pay_bank
        self.pay_tax = pay_tax
        self.pay_agree = pay_agree
        self.pay_confirm = pay_confirm

class account:
    def __init__(self, id, pwd, pNum_p1, pNum_p2, pNum_p3):
        self.id = id
        self.pwd = pwd
        self.pNum_p1 = pNum_p1
        self.pNum_p2 = pNum_p2
        self.pNum_p3 = pNum_p3

class common:
    def __init__(self, soundV, soundD, selSat, selSun, dayConfirm):
        self.soundV = soundV
        self.soundD = soundD
        self.selSat = selSat
        self.selSun = selSun
        self.dayConfirm = dayConfirm

class login:
    def __init__(self, loginBtn, loginMelon, loginId, loginPwd, loginSubmit):
        self.loginBtn = loginBtn
        self.loginMelon = loginMelon
        self.loginId = loginId
        self.loginPwd = loginPwd
        self.loginSubmit = loginSubmit

comm = common(soundV=500, soundD=3000
              , selSat='/html/body/div/div[3]/div/div/div/div[1]/div[2]/div/div[1]/dl[1]/dd[2]/div[1]/ul/li[1]/button'
              , selSun='/html/body/div/div[3]/div/div/div/div[1]/div[2]/div/div[1]/dl[1]/dd[2]/div[1]/ul/li[2]/button'
              , dayConfirm='/html/body/div/div[3]/div/div/div/div[1]/div[2]/div/div[2]/div/div[2]/button/span')

dongbin = account(id='rewgh0', pwd='sodwkdrh12@', pNum_p1='010', pNum_p2='8632', pNum_p3='3505')
luv = account(id='luvme301', pwd='musical!04', pNum_p1='010', pNum_p2='8632', pNum_p3='3505')

login = login(loginBtn='/html/body/div/div[2]/div/div[1]/div[1]/div[2]/ul/li[2]/span/a'
              , loginMelon='/html/body/div/div[2]/div/div/div/div[2]/button'
              , loginId='/html/body/div/div[2]/div/div/div/div[1]/div/input[1]'
              , loginPwd='/html/body/div/div[2]/div/div/div/div[1]/div/input[2]'
              , loginSubmit='/html/body/div/div[2]/div/div/div/div[2]/button')

IU_ALL = ticket(url='https://ticket.melon.com/performance/index.htm?prodId=210230'
              , openSeat_V='/html/body/div/div[2]/div[2]/div/div[1]/div/table/tbody/tr[1]/td[4]'
              , openSeat_R='/html/body/div/div[2]/div[2]/div/div[1]/div/table/tbody/tr[3]/td[4]'
              , openSeat_S="/html/body/div/div[2]/div[2]/div/div[1]/div/table/tbody/tr[5]/td[4]"
              , openSeat_A='/html/body/div/div[2]/div[2]/div/div[1]/div/table/tbody/tr[7]/td[4]'
              , openSeat_B='/html/body/div/div[2]/div[2]/div/div[1]/div/table/tbody/tr[11]/td[4]'
              , zoneCount_V=19
              , zoneCount_R=13
              , zoneCount_S=18
              , zoneCount_A=19
              , zoneCount_B=17
              , zoneSelect_V1='/html/body/div/div[2]/div[2]/div/div[1]/div/table/tbody/tr[2]/td/div/ul/li['
              , zoneSelect_V2=']/span[2]/strong'
              , zoneSelect_R1='/html/body/div/div[2]/div[2]/div/div[1]/div/table/tbody/tr[4]/td/div/ul/li['
              , zoneSelect_R2=']/span[2]/strong'
              , zoneSelect_S1='/html/body/div/div[2]/div[2]/div/div[1]/div/table/tbody/tr[6]/td/div/ul/li['
              , zoneSelect_S2=']/span[2]/strong'
              , zoneSelect_A1='/html/body/div/div[2]/div[2]/div/div[1]/div/table/tbody/tr[8]/td/div/ul/li['
              , zoneSelect_A2=']/span[2]/strong'
              , zoneSelect_B1='/html/body/div/div[2]/div[2]/div/div[1]/div/table/tbody/tr[12]/td/div/ul/li['
              , zoneSelect_B2=']/span[2]/strong'
              , resetSeat='/html/body/div/div[2]/div[2]/div/h3/a/span'
              , imgName='A.png'
              , seatConfirm='/html/body/div/div[2]/div[3]/div/span/a'
              , ticketCnt='/html/body/div/div[1]/div[2]/div[1]/div/div[1]/div/div/div/dl/dd[3]/select'
              , ticketConfirm='/html/body/div/div[2]/div[3]/div[2]/span[2]/a'
              , pay_num1='/html/body/div[2]/div[1]/div[2]/form/div[1]/div[2]/div/table/tbody/tr[1]/td[2]/div/input[2]'
              , pay_num2='/html/body/div[2]/div[1]/div[2]/form/div[1]/div[2]/div/table/tbody/tr[1]/td[2]/div/input[3]'
              , pay_num3='/html/body/div[2]/div[1]/div[2]/form/div[1]/div[2]/div/table/tbody/tr[1]/td[2]/div/input[4]'
              , pay_type='/html/body/div[2]/div[1]/div[2]/form/div[3]/ul/li[2]/label/input'
              , pay_bank='/html/body/div[2]/div[1]/div[2]/form/div[3]/div[2]/div/table/tbody/tr[1]/td/div/div/select'
              , pay_tax='/html/body/div[2]/div[1]/div[2]/form/div[3]/div[2]/div/table/tbody/tr[3]/td/ul/li[3]/input'
              , pay_agree='/html/body/div[2]/div[1]/div[2]/form/div[4]/ul/li[1]/div/div/input'
              , pay_confirm='/html/body/div[2]/div[2]/div[3]/div[2]/span[2]/a'
              )