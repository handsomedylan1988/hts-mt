#!/usr/bin/env perl 
#===============================================================================
#
#         FILE: interpolate.pl
#
#        USAGE: ./interpolate.pl  
#
#  DESCRIPTION: interpolate the f0
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: Ran Zhang (Dr.), zran1988@outlook.com
# ORGANIZATION: 
#      VERSION: 1.0
#      CREATED: 2016年04月22日 21时26分47秒
#     REVISION: ---
#===============================================================================

use strict;
use warnings;
use utf8;
use Getopt::Std;

use vars qw($opt_i $opt_o);
getopts("i:o:");

die "please specify input lf0 file" if not defined $opt_i;

my $infile=$opt_i;
open IN ,$infile or die $!;
binmode(IN);
seek(IN,0,2);
my $len=tell(IN);
seek(IN,0,0);

my $buf;
read(IN,$buf,$len);
my @lf0s=unpack("f" x ($len/4), $buf);
push @lf0s,0;
unshift @lf0s,0;
my $vflag=1;
my ($sidx,$eidx);
my @vflags;
for(my $i=0;$i<=$#lf0s;$i++)
{
    if($lf0s[$i]==-1e10)
    {
        if($vflag==1)
        {
            $sidx=$i-1;
        }
        $vflag=0;
    }
    else
    {
        if($vflag==0)
        {
            $eidx=$i;
            my $delta=($lf0s[$eidx]-$lf0s[$sidx])/($eidx-$sidx);
            for(my $j=$sidx+1;$j<=$eidx-1;$j++)
            {
                $lf0s[$j]=$lf0s[$sidx]+$delta*($j-$sidx);
            }
        }
        $vflag=1;

    }
    push @vflags,$vflag;
}
pop @lf0s;
shift @lf0s;
pop @vflags;
shift @vflags;

$buf=pack("f" x ($len/4),@lf0s);

print $buf;

#-------------------------------------------------------------------------------
#  output uvinformation if -o is set
#-------------------------------------------------------------------------------
if(defined $opt_o)
{
    open OUT,">$opt_o";
    $buf=pack("f" x ($len/4),@vflags);
    print OUT $buf;
    close(OUT);
}

