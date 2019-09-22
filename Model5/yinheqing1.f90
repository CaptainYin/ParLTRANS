program main
use mpi
DOUBLE PRECISION f(10,2)

integer code,np,world,ierr
do i=1,10
f(i,1)=1
f(i,2)=2
enddo

call mpi_init(ierr)
call mpi_comm_dup(mpi_comm_world,world,ierr)
call mpi_comm_rank(world,code,ierr)
call mpi_comm_size(world,np,ierr)
do i=1,3
call update()
if(code.eq.0)then

    print*,'global f',f
endif
enddo
call mpi_comm_free(world,ierr)
call mpi_finalize(ierr)
contains

subroutine update()


integer i,j,istr,iend,avgtask,extra,currtasknum
double precision, allocatable :: kf(:,:)
character*8 name

!parallel


avgtask=10/np
extra=mod(10,np)
!print*,'extra',extra 
if(code .lt. extra)then
        istr=(avgtask+1)*code+1
        iend=(avgtask+1)*(code+1)
        currtasknum=avgtask+1
else
        istr=avgtask*code+1+extra
        iend=avgtask*(code+1)+extra
        currtasknum=avgtask
endif
print*,'code,istr,iend',code,',',istr,',',iend
do i=istr,iend
f(i,1)=f(i,1)+10*code
f(i,2)=f(i,2)+10*code
enddo
if(code.eq.0)then
allocate(kf(10,2))
endif

call mpi_gather(f(istr,1),2*currtasknum,mpi_integer,kf(istr,1),2*currtasknum,mpi_integer,0,world,ierr)
call mpi_gather(f(istr,2),2*currtasknum,mpi_integer,kf(istr,2),2*currtasknum,mpi_integer,0,world,ierr)

if(code.eq.0)then
        f=kf
     !   print*,'dddddddd',f
        deallocate(kf)
endif


end subroutine update

end program
