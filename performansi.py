class Performansi:
    def track(self, employees, hours):
        print('Perekaman Produktivitas Karyawan')
        print('==============================')
        for employee in employees:
            employee.work(hours)
        print('')