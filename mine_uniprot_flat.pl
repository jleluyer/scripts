#/usr/bin/perl

#####
## Author: Frederic Fournier
## Date: 2013-02-25
## Goal:
##   Data-mine an uniprot 'flat-text retrieve' based on Jeremy's input list
##   and get information about gene and GO annotation. 
####


## Open file handles
## Uncomment necessary handles and adjust file location:

open INPUT_FILE1, "<", "/home/leyjer01/UniprotRetrieveEST.txt" or die $!;
open OUTPUT_FILE1, ">", "/home/leyjer01/no_GN.txt" or die $!;
open OUTPUT_FILE2, ">", "/home/leyjer01/no_GO.txt" or die $!;
open OUTPUT_FILE3, ">", "/home/leyjer01/both_GO_and_GN.txt" or die $!;

## Setup variables

my $line_count=0;
my $GN=0;
my $GO=0;
my $ID="";

## READ INPUT 
while (<INPUT_FILE1>) {
    chomp;
    if ($_ =~ /^\/\// ) {
	unless ($GN) {print OUTPUT_FILE1 "$ID\n";}
	unless ($GO) {print OUTPUT_FILE2 "$ID\n";}
	if ( $GN && $GO ) {print OUTPUT_FILE3 "$GN\n";}
	$GN=0;
	$GO=0;
	$ID="";
    }
    elsif ($_ =~ /^ID/ ) {
	my @ID_a = split(/\s+/, $_);
	$ID= $ID_a[1]
    }
    elsif ($_ =~ /^GN\s+Name=(.*?);/) {
	$GN = $1;
    }
    elsif ($_ =~ /DR\s+GO/ ) {
	$GO=1;
    }
}

## Close file handles
## Uncomment necessary handles:

close INPUT_FILE1 or die $!;
close OUTPUT_FILE1 or die $!;
close OUTPUT_FILE2 or die $!;
close OUTPUT_FILE3 or die $!;

