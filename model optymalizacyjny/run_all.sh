for i in $(seq 1 $1);
do
    mv "generated_data$i.dat" "generated_data.dat";
    ampl "ampl_create_data.run";
    rm -r "./rozwiązania/data$i/";
    mkdir "./rozwiązania/data$i";
    mv "./rozwiązania/"*".txt" "./rozwiązania/data$i";
    mv "generated_data.dat" "generated_data$i.dat";
done