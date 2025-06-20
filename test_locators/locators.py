from selenium.webdriver.common.by import By


class LoginPageLocators:
    login_email_id=(By.ID,"login_email")
    login_password_id=(By.ID,"login_password")
    signup_name_id=(By.ID,"signup_name")
    forgot_password_email=(By.ID, "forgot-password_email")
    remember_me_id=(By.ID, "login_remember")

    login_button_css =(By.CSS_SELECTOR,"button[type='submit']")

    create_project_xpath= (By.XPATH,"//button[span[normalize-space()='Create Project']]")
    signup_link_xpath = (By.XPATH,"//a[text()='Sign up']")
    email_error_notify_xpath=(By.XPATH,"//div[text()='Please enter a valid email address']")
    empty_error_notify_xpath=(By.XPATH,"//div[@class='ant-notification-notice-description' and text()='Please check your email and password and try again']")
    eye_icon_xpath =(By.XPATH,"//span[contains(@class, 'ant-input-password-icon') and @aria-label='eye']")
    forgot_password_link_xpath =(By.XPATH, "//a[text()='Forgot password?']")
    reset_password_button_xpath =(By.XPATH, "//button[span[text()='Reset Password']]")
    return_to_login_button_xpath=(By.XPATH, "//button[span[text()='Return to Login']]")
    account_does_not_exist_error =(By.XPATH, "//div[contains(@class, 'ant-notification-notice-description') and text()='Account does not exists!']")
    email_empty_notification=(By.XPATH, "//div[@class='ant-form-item-explain-error' and text()='Please enter your Email!']")
    signin_with_google_xpath=(By.XPATH, "//button[span[text()='Sign in with Google']]")


class HomePageLocators:
    nav_bar_xpath = (By.XPATH,"//ul[@role='menu']")
    invite_button_xpath=(By.XPATH,"//button[span[text()='Invite']]")
    notification_icon_xpath=(By.XPATH,"//button[.//span[@aria-label='bell']]")
    help_button_xpath=(By.XPATH,"//button[.//span[@aria-label='question-circle']]")
    profile_xpath=(By.XPATH,"//span[@aria-label='user']//*[name()='svg']")
    create_project_xpath = (By.XPATH, "//button[span[normalize-space()='Create Project']]")
    expan_button_css = (By.CSS_SELECTOR,"button[class='ant-btn css-1vhso2s ant-btn-primary ant-btn-color-primary ant-btn-variant-solid ant-btn-icon-only ant-btn-compact-item ant-btn-compact-last-item ant-dropdown-trigger ant-dropdown-open']")
    import_template_xpath=(By.XPATH,"//li[@class='ant-dropdown-menu-item ant-dropdown-menu-item-only-child' and contains(., 'Import from template')]")
    name_xpath=(By.XPATH,"//h3[@class='ant-typography css-1vhso2s' and text()='Hi Asaliee, Good morning!']")
    date_css=(By.CSS_SELECTOR,"h4[class='ant-typography css-1vhso2s']")
    task_table_xpath=(By.XPATH,"//div[@data-node-key='All' and contains(@class, 'ant-tabs-tab-active')]")
    list_tab_xpath=(By.XPATH,"//div[@class='ant-segmented-item-label' and @title='List' and text()='List' and @aria-selected='true']")
    calender_tab_xpath=(By.XPATH,"//div[@class='ant-segmented-item-label' and @title='Calendar' and text()='Calendar' and @aria-selected='false']")
    Month_xpath=(By.XPATH,"//span[@class='ant-radio-button-label' and text()='Month']")
    current_year_xpath=(By.XPATH,"//span[@class='ant-select-selection-item' and @title='2025' and text()='2025']")
    current_month_xpath=(By.XPATH,"//div[contains(@class, 'ant-picker-calendar-month-select')]//span[@class='ant-select-selection-item' and @title='Apr']")
    year_xpath=(By.XPATH,"//span[@class='ant-radio-button-label' and text()='Year']")
    assigned_to_me_button_xpath=(By.XPATH,"//span[@class='ant-select-selection-item' and @title='Assigned to me' and text()='Assigned to me']")
    refresh_button_xpath=(By.XPATH,"//button[@type='button' and .//span[@role='img' and contains(@class, 'anticon-sync')]]")
    to_do_list_xpath=(By.XPATH,"//form[@class='ant-form ant-form-horizontal css-1vhso2s']")
    add_task_todo_xpath=(By.XPATH,"//input[@placeholder='+ Add Task']")
    todo_refresh_xpath=(By.XPATH,"//div[contains(@class,'ant-card-head-extra')]//button[@type='button']//span[@aria-label='sync']")
    project_table_xpath=(By.XPATH,"//h5[@class='ant-typography css-1vhso2s' and text()='Projects']")
    favourite_icon_xpath=(By.XPATH,"//svg[@data-icon='star']")
    favourite_icon_favourite_xpath=(By.XPATH,"//span[@role='img' and @aria-label='star' and contains(@class, 'anticon-star')]")
    recent_tab_xpath=(By.XPATH,"//div[@class='ant-segmented-item-label' and text()='Recent']")
    favourite_tab_xpath=(By.XPATH,"//div[@class='ant-segmented-item-label' and text()='Favourites']")
    project_refresh_xpath=(By.XPATH,"//svg[@data-icon='sync']")
    switch_team_xpath=(By.XPATH,"//div[contains(@class, 'ant-dropdown-trigger') and contains(@class, 'ant-flex') and contains(@class, 'ant-flex-align-center') and contains(@class, 'ant-flex-justify-center')]")
    task_raw_name_xpath=(By.XPATH,"//span[contains(@class, 'ant-typography') and contains(@class, 'ant-tooltip-open')]")
    task_raw_open_xpath=(By.XPATH,"//button[@type='button' and contains(@class, 'ant-btn') and .//span[@role='img' and contains(@class, 'anticon-expand-alt')]]")
    task_raw_project_xpath=(By.XPATH,"//div[contains(@class, 'ant-typography') and contains(@class, 'ant-tooltip-open') and span[contains(@class, 'ant-badge-status-dot')]]")
    mark_as_done_xpath=(By.XPATH,"//svg[@data-icon='check-circle']")
    task_in_todo_list_xpath=(By.XPATH,"//span[contains(@class, 'ant-tooltip-open')]")
    create_project_drawer_xpath=(By.XPATH,"//div[contains(@class, 'ant-drawer-title')]/span[contains(@class, 'ant-typography')]")


    project_name_css=(By.CSS_SELECTOR,"div[id=':r89:']")


class ProjectDrawerUILocators:

    health_id=(By.ID,"health_id")

    client_name_id=(By.ID,"client_name")
    start_date_id=(By.ID,"start_date")
    project_health_id = (By.ID, "health_id")



    status_css=(By.CSS_SELECTOR,"body > div:nth-child(4) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)")
    name_field_xpath=(By.XPATH,"//input[@id='name']")
    create_project_xpath = (By.XPATH, "//span[normalize-space()='Create']")

    status_dropdown_css=(By.CSS_SELECTOR,".ant-select-item.ant-select-item-option.ant-select-item-option-active")
    health_dropdown_css=(By.CSS_SELECTOR,"div[class='ant-select-dropdown ant-slide-up-leave ant-slide-up-leave-active ant-slide-up css-1vhso2s ant-select-dropdown-placement-bottomLeft'] div div[class='rc-virtual-list'] div[class='rc-virtual-list-holder'] div div[class='ant-select-item ant-select-item-option ant-select-item-option-active'] span[class='ant-typography css-1vhso2s']")
    new_category_css=(By.CSS_SELECTOR,"div[class='ant-select-dropdown ant-slide-up-leave ant-slide-up-leave-active ant-slide-up css-1vhso2s ant-select-dropdown-empty ant-select-dropdown-placement-bottomLeft'] span:nth-child(2)")
    create_category_button_css=(By.CSS_SELECTOR,"button[class='ant-btn css-1vhso2s ant-btn-primary ant-btn-color-primary ant-btn-variant-solid'] span")
    category_css = (By.CSS_SELECTOR,".ant-select.ant-select-outlined.ant-select-in-form-item.css-1vhso2s.ant-select-single.ant-select-allow-clear.ant-select-show-arrow")
    project_page_css=(By.CSS_SELECTOR,"a[href='/worklenz/projects']")
    table_name_css=(By.CSS_SELECTOR,"th[aria-label='Name'] span[class='ant-table-column-title']")
    name_empty_error_css=(By.CSS_SELECTOR,".ant-form-item-explain-error")
    down_element_button_css=(By.CSS_SELECTOR,"span[class='anticon anticon-down']")
    create_from_temp_button_css=(By.CSS_SELECTOR,".w-full.m-0.p-0")
    drawer_title_css=(By.CSS_SELECTOR,".ant-drawer-title")

    color_picker_css=(By.CSS_SELECTOR,"input[value='164c9b']")
    colour_dropdown_css = (By.CSS_SELECTOR, "#color_code")
    project_category_css=(By.CSS_SELECTOR,"label[title='Category']")
    add_category_button_css=(By.CSS_SELECTOR,"div[class='ant-select-dropdown ant-slide-up-leave ant-slide-up-leave-active ant-slide-up css-avcqrf ant-select-dropdown-placement-bottomLeft'] div button[type='button']")
    add_category_css=(By.CSS_SELECTOR,"body > div:nth-child(8)")
    project_note_xpath=(By.XPATH,"//label[normalize-space()='Notes']")




class CreatedProject:
    task_list_css=(By.CSS_SELECTOR,"div[id='rc-tabs-0-tab-tasks-list'] div[class='ant-flex css-avcqrf ant-flex-align-center']")
    create_task_button_css=(By.CSS_SELECTOR,"button[class='ant-btn css-13y8tqx ant-btn-primary ant-btn-color-primary ant-btn-variant-solid ant-btn-compact-item ant-btn-compact-first-item']")
    back_button_css=(By.CSS_SELECTOR,"svg[viewBox='64 64 896 896'][focusable='false'][data-icon='arrow-left']")
    table_header_name_css=(By.CSS_SELECTOR,"th[aria-label='Name']")
    table_column_css=(By.CSS_SELECTOR,".ant-table-cell.ant-table-column-sort.ant-table-cell-row-hover")
    # .flex.items - center


class ImportFromTemp:
    worklenz_library_tab_css = (By.CSS_SELECTOR, "#rc-tabs-0-tab-1")
    temp_list_css=(By.CSS_SELECTOR,".ant-menu.ant-menu-root.ant-menu-inline.ant-menu-light.template-menu.css-13y8tqx")
    create_button_css=(By.CSS_SELECTOR,"button[class='ant-btn css-13y8tqx ant-btn-primary ant-btn-color-primary ant-btn-variant-solid']")
    task_list_css=(By.CSS_SELECTOR,"div[id='rc-tabs-1-tab-tasks-list'] div[class='ant-flex css-13y8tqx ant-flex-align-center']")


class TaskTable:
    add_task_button_css=(By.CSS_SELECTOR,"input[placeholder='+ Add task']")


class ProjectUI:
    project_tab_css=(By.CSS_SELECTOR,"a[href='/worklenz/projects']")
    all_tab_css=(By.CSS_SELECTOR,"div[title='All']")
    favourite_tab_css=(By.CSS_SELECTOR,"div[title='Favorites']")
    archive_tab_css=(By.CSS_SELECTOR,"div[title='Archived']")
    personal_xpath=(By.XPATH,"//span[contains(text(),'Personal use')]")
    favourite_icon_css=(By.CSS_SELECTOR,"span[aria-label='star']")
    refresh_button_css=(By.CSS_SELECTOR,"button[aria-label='Refresh projects'] span[class='ant-btn-icon']")
    search_by_name_css=(By.CSS_SELECTOR,"input[placeholder='Search by name']")
    create_project_button_css=(By.CSS_SELECTOR,"body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > main:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > button:nth-child(1) > span:nth-child(2)")
    drop_down_css=(By.CSS_SELECTOR,"span[class='anticon anticon-down']")
    import_from_temp_css=(By.CSS_SELECTOR,".w-full.m-0.p-0")
    edu_row_css=(By.CSS_SELECTOR,"body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > main:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(3) > tr:nth-child(1) > td:nth-child(2) > div:nth-child(1) > span:nth-child(2) > span:nth-child(1)")

    construction_project_css=(By.CSS_SELECTOR,"body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > main:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(3) > tr:nth-child(1) > td:nth-child(2) > div:nth-child(1) > span:nth-child(2) > span:nth-child(1)")
    subscribe_button_css=(By.CSS_SELECTOR,"body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > main:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(4) > span:nth-child(2)")
    project_name_xpath=(By.XPATH,"//h4[normalize-space()='Construction']")
    project_refresh_button = (By.CSS_SELECTOR,"svg[viewBox='64 64 896 896'][focusable='false'][data-icon='sync']")
    save_temp_css=(By.CSS_SELECTOR,"svg[viewBox='64 64 896 896'][focusable='false'][data-icon='save']")
    settings_button_css = (By.CSS_SELECTOR,"button[class='ant-btn css-avcqrf ant-btn-circle ant-btn-default ant-btn-color-default ant-btn-variant-outlined ant-btn-icon-only ant-tooltip-open'] span[aria-label='setting']")
    invite_button_css = (By.CSS_SELECTOR,"button[class='ant-btn css-avcqrf ant-btn-primary ant-btn-color-primary ant-btn-variant-solid'] span[aria-label='usergroup-add'] svg path")







# python -m pytest test_cases/test_login/test_login.py


