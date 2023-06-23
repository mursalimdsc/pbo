import hr
import karyawan
import performansi

salary_employee = hr.GajiPegawai(1, 'Fila Kurnia', 15000000)
hourly_employee = hr.PegawaiJam(2, 'Riskon Silalahi', 40, 15)
commission_employee = hr.KomisiPegawai(3, 'Heru Santoso', 1000000, 250000)
payroll_system = hr.SistemPenggajian()
payroll_system.calculate_payroll([
    salary_employee,
    hourly_employee,
    commission_employee
])

manager = karyawan.Manager(1, 'Ageng Bagus Sadewo', 3000000)
secretary = karyawan.Secretary(2, 'Ulil Absor Maulana', 1500000)
sales_guy = karyawan.SalesPerson(3, 'Dwi Maulana Hetapea', 1000000, 200000)
factory_worker = karyawan.FactoryWorker(2, 'Lutfi Ardi Slamet', 40, 15)
employees = [manager,secretary,sales_guy,factory_worker]
productivity_system = performansi.Performansi()
productivity_system.track(employees, 40)
payroll_system = hr.SistemPenggajian()
payroll_system.calculate_payroll(employees)