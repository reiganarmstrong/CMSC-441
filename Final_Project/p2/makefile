factor: factor.o
	clang++ factor.o -lgmpxx -lgmp -o factor
factor.o: factor.cpp
	clang++ -c factor.cpp 
run:
	./factor
clean:
	rm *.o factor