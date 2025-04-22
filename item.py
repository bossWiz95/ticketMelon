
class ticket:
    def __init__(self, url, openSeat_V, openSeat_R, openSeat_S, openSeat_A, openSeat_B, zoneCount_V, zoneCount_R, zoneCount_S, zoneCount_A, zoneCount_B,  zoneSelect_R1, zoneSelect_R2,
                 zoneSelect_V1, zoneSelect_V2, zoneSelect_S1, zoneSelect_S2, zoneSelect_A1, zoneSelect_A2, zoneSelect_B1, zoneSelect_B2, resetSeat, seatConfirm):
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
        self.seatConfirm = seatConfirm

class account:
    def __init__(self, id, pwd, pNum_p1, pNum_p2, pNum_p3):
        self.id = id
        self.pwd = pwd
        self.pNum_p1 = pNum_p1
        self.pNum_p2 = pNum_p2
        self.pNum_p3 = pNum_p3

class common:
    def __init__(self, soundV, soundD, sel1, sel2, sel3, dayConfirm):
        self.soundV = soundV
        self.soundD = soundD
        self.sel1 = sel1
        self.sel2 = sel2
        self.sel3 = sel3
        self.dayConfirm = dayConfirm

class login:
    def __init__(self, loginBtn, loginMelon, loginId, loginPwd, loginSubmit):
        self.loginBtn = loginBtn
        self.loginMelon = loginMelon
        self.loginId = loginId
        self.loginPwd = loginPwd
        self.loginSubmit = loginSubmit

comm = common(soundV=500, soundD=3000
              , sel1='/html/body/div/div[3]/div/div/div/div[1]/div[2]/div/div[1]/dl[1]/dd[2]/div[2]/div/a[2]'
              , sel2='/html/body/div/div[3]/div/div/div/div[1]/div[2]/div/div[1]/dl[1]/dd[2]/div[2]/table/tbody/tr[2]/td[7]/button'
              , sel3='/html/body/div/div[3]/div/div/div/div[1]/div[2]/div/div[1]/dl[2]/dd/div/ul/li/button/p'
              # , sel3='/html/body/div/div[3]/div/div/div/div[1]/div[2]/div/div[1]/dl[2]/dd/div/ul/li[1]/button/span'
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
              , seatConfirm='/html/body/div/div[2]/div[3]/div/span/a'
              )

pt = ticket(url='https://ticket.melon.com/performance/index.htm?prodId=211212'
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
              , seatConfirm='/html/body/div/div[2]/div[3]/div/span/a'
              )