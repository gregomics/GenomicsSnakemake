# GenomicsSnakemake

This is a repository for the genomics workflows based on Snakemake workflow managment system.
More information can be found in [snakemake readthedocs](https://snakemake.readthedocs.io/en/stable/).

# Requirements

  * snakemake version 5.1.5
  * tools that you want to execute (e.g. bowtie2/hisate2 and so on)
  * fastq-mcf or cutadapt (adapter trimmer)
  * hisat2 (RNAseq) 
  * bwa/bowtie2 (other genomics application)
  * macs2 (peak caller)
  * featureCount (RNAseq)

## Getting Started

An RNAseq workflow is defined in the RNAseq directory.
  * workflow.py: defines the set of rules that are applied
  * config.yml: yaml file that defines the configuration and parameters for the rules


```{shell}
cd RNAseq/
snakemake -s workflow.py

```

## Running under SLURM

Snakemake workflow can be run on the HPC using SLURM (or other scheduler).
For SLURM here is the command that can be used:

```{shell}
snakemake -j 999 --cluster-config cluster.json --latency-wait 60 --cluster "sbatch -t 200 --error slurm.err " -s workflow.py

```
The advantage of using a configuration file (e.g. cluster.json) is that each rule can have a different setting.
All the parameter from the json file can be accessed using {cluster.paramater}.
Note: The latency time needs to be increase for completion.

# References

Köster, Johannes and Rahmann, Sven. "Snakemake - A scalable bioinformatics workflow engine". Bioinformatics 2012.

