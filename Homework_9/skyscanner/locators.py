from selenium.webdriver.common.by import By

# destination input
DEST_INP = (By.CSS_SELECTOR, '#fsc-destination-search')

# destination dropdown - value No.1
DEST_DRDOWN_VAL_0 = (By.CSS_SELECTOR, '#react-autowhatever-fsc-destination-search--item-0')

"""Departure and Return inputs"""
# departure date input
DEP_DATE_INPUT = (By.CSS_SELECTOR, "#depart-fsc-datepicker-button")

# return date input
RET_DATE_INPUT = (By.CSS_SELECTOR, "#return-fsc-datepicker-button")

"""Departure and Return months"""
# departure month dropdown
DEP_MONTH_DRDOWN = "#depart-calendar__bpk_calendar_nav_select"

# return month dropdown
RET_MONTH_DRDOWN = "#return-calendar__bpk_calendar_nav_select"

"""Departure and Return month calendars"""
# departure calendar
DEP_CALENDAR = ".BpkCalendarGrid_bpk-calendar-grid__sak14.FlightDatepicker_fsc-datepicker__list-size__1UX2a"

# return calendar
RET_CALENDAR = ".BpkCalendar_bpk-calendar__1MP0A.FlightDatepicker_fsc-datepicker__calendar__UTmOD" \
               ".BpkCalendar_bpk-calendar--fixed__3kFGk"

# direct fly checkbox
DIR_FLY_CHBOX = '.BpkCheckbox_bpk-checkbox__input__1deNR[name="directOnly"]'

# find fly button
FIND_FLY_BTN = '.BpkButtonBase_bpk-button__1pnhi'

# departure left slider
DEP_LFT_SLIDER = "/html//dd[@id='departure-times_content']/div/div/div[1]/div/div[4]"

# departure right slider
DEP_RHT_SLIDER = "/html//dd[@id='departure-times_content']/div/div/div[1]/div/div[5]"

# return left slider
RET_LFT_SLIDER = "/html//dd[@id='departure-times_content']/div/div/div[2]/div/div[4]"

# return right slider
RET_RHT_SLIDER = "/html//dd[@id='departure-times_content']/div/div/div[2]/div/div[5]"