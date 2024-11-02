import magicube_adder as ma
import magicube as m
import traversal as t

n: int = 5

# Menerima input dari pengguna untuk jumlah maksimum iterasi
x = int(input("Enter the maximum iteration: "))
MAX_ITERATION: int = x

cube: m.Magicube = m.Magicube(n)

def generate_vector(n: int, size: int) -> t.Vector3:
    return t.Vector3([n % size, n // (size) % size, n // (size**2)])

try:
    for i in range(MAX_ITERATION):
        current_fitness = ma.fitness(cube)
        
        print(f"Iteration {i + 1} - Starting fitness: {current_fitness}")
        
        # Memeriksa apakah kubus saat ini sudah optimal
        if current_fitness >= 0.0:
            print("Optimal solution found.")
            break
        
        found_better = False
        best_cube = cube.copy()
        best_fitness = current_fitness

        for j in range(n**3 - 1):
            start = generate_vector(j, n)

            for k in range(j + 1, n**3):
                target = generate_vector(k, n)
                
                # Menukar posisi dengan yang nilai fitness lebih baik
                cube.swap_spot(start.x, start.y, start.z, target.x, target.y, target.z)
                
                # Menghitung fitness setelah swap
                new_fitness = ma.fitness(cube)
                
                # Jika konfigurasi baru lebih baik, simpan
                if new_fitness > best_fitness:
                    best_fitness = new_fitness
                    found_better = True
                    best_cube = cube.copy()
                    print(f"NEW: {best_fitness} >> Current fitness after swap: {ma.fitness(cube)}")
                
                # Kembalikan swap
                cube.swap_spot(start.x, start.y, start.z, target.x, target.y, target.z)
        
        # Memperbarui kubus jika ditemukan konfigurasi yang lebih baik
        if found_better:
            cube = best_cube
            print(f"End of iteration {i + 1} - New best fitness: {best_fitness}")
        else:
            print(f"End of iteration {i + 1} - No better solution found, stopping.")
            break  # Berhenti jika tidak ada solusi yang lebih baik

        print(f"Current fitness after iteration {i + 1}: {ma.fitness(cube)}\n")

    # Mencetak konfigurasi akhir kubus setelah iterasi terakhir
    print("Final cube configuration:")
    cube.print()

except Exception as e:
    print("An error occurred:", e)
    cube.print()
