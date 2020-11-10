import functs


def main():
    functs.cred_gen()
    functs.service_gen()
    functs.show_event_id()
    if functs.volunteer_or_student() == "student":
        pass
    else :
        summary = functs.summary_input()
        loc = functs.location_input()
        vol = functs.user_email()
        start_time_volunteer = functs.time_slot_volunteer()
        year,month,day,hour,minute,second = start_time_volunteer
        date = datetime(year,month,day,hour,minute,second)
        end_time_volunteer = date + timedelta(hours=1, minutes=30)
        # print (date)
        # print (end_time_volunteer)
        # desc = desc_input()
        create_event_voluteer_slots(summary, loc, vol, date, end_time_volunteer)


if __name__ == '__main__':
    main()