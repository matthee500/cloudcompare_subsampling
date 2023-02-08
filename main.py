import os
import subprocess


def cloud_compare_merge(direct, cc):
    i = 1
    merge = []
    merged_directory = direct + '\\merged'
    if not os.path.exists(merged_directory):
        os.makedirs(merged_directory)

    for file_dir in os.listdir(direct):
        d = os.path.join(direct, file_dir)
        if os.path.isdir(d):
            if len(os.listdir(d)) == 0:
                continue

            else:
                merge.append(cc)
                merge.append('-SILENT')
                merge.append('-NO_TIMESTAMP')
                merge.append('-AUTO_SAVE')
                merge.append('OFF')
                merge.append('-C_EXPORT_FMT')
                merge.append('E57')

                for filename in os.listdir(d):
                    file_ptx = os.path.join(d, filename)
                    if os.path.isfile(file_ptx):
                        if file_ptx.endswith('.ptx'):
                            merge.append('-O')
                            merge.append('-GLOBAL_SHIFT')
                            merge.append('AUTO')
                            merge.append(file_ptx)

                merge.append('-MERGE_CLOUDS')
                merge.append('-DROP_GLOBAL_SHIFT')
                merge.append('-SAVE_CLOUDS')
                merge.append('FILE')
                cc_saved = merged_directory + '\\' + 'processed' + str(i) + '.e57'
                merge.append(cc_saved)
                subprocess.check_call(merge, shell=True)
                i += 1
                merge.clear()


def cloud_compare_ss(direct, cc):
    ss_1 = 1
    processed_directory = direct + '\\merged'
    sub_sampled_directory = direct + '\\processed'
    if not os.path.exists(sub_sampled_directory):
        os.makedirs(sub_sampled_directory)

    for filename in os.listdir(processed_directory):
        file = os.path.join(processed_directory, filename)
        if os.path.isfile(file):
            if file.endswith('.e57'):
                cc_saved = sub_sampled_directory + '\\' + 'merged_sampled' + str(ss_1) + '.e57'
                subprocess.check_call([cc, '-SILENT', '-NO_TIMESTAMP', '-AUTO_SAVE', 'OFF', '-C_EXPORT_FMT', 'E57',
                                       '-O', '-GLOBAL_SHIFT', 'AUTO', file, '-SS', 'SPATIAL', '0.004',
                                       '-DROP_GLOBAL_SHIFT', '-SAVE_CLOUDS', 'FILE', cc_saved], shell=True)
                ss_1 += 1


def cloud_compare_final_merge(direct, cc):
    final_merge = []
    sub_sampled_directory = direct + '\\processed'
    final_merged_directory = direct + '\\final_merge'

    if not os.path.exists(final_merged_directory):
        os.makedirs(final_merged_directory)
        final_merge.append(cc)
        final_merge.append('-SILENT')
        final_merge.append('-NO_TIMESTAMP')
        final_merge.append('-AUTO_SAVE')
        final_merge.append('OFF')
        final_merge.append('-C_EXPORT_FMT')
        final_merge.append('E57')

        for filename in os.listdir(sub_sampled_directory):
            file_e57 = os.path.join(sub_sampled_directory, filename)
            if os.path.isfile(file_e57):
                if file_e57.endswith('.e57'):
                    final_merge.append('-O')
                    final_merge.append('-GLOBAL_SHIFT')
                    final_merge.append('AUTO')
                    final_merge.append(file_e57)

        final_merge.append('-MERGE_CLOUDS')
        final_merge.append('-DROP_GLOBAL_SHIFT')
        final_merge.append('-SAVE_CLOUDS')
        final_merge.append('FILE')
        cc_saved = final_merged_directory + '\\final_merge.e57'
        final_merge.append(cc_saved)
        subprocess.check_call(final_merge, shell=True)
        final_merge.clear()


def cloud_compare_final_ss(direct, cc):
    processed_directory = direct + '\\final_merge'
    sub_sampled_directory = direct + '\\final_processed'
    if not os.path.exists(sub_sampled_directory):
        os.makedirs(sub_sampled_directory)

    for filename in os.listdir(processed_directory):
        file = os.path.join(processed_directory, filename)
        if os.path.isfile(file):
            if file.endswith('.e57'):
                cc_saved = sub_sampled_directory + '\\' + 'final_merged_sampled.e57'
                subprocess.check_call([cc, '-SILENT', '-NO_TIMESTAMP', '-AUTO_SAVE', 'OFF', '-C_EXPORT_FMT', 'E57',
                                       '-O', '-GLOBAL_SHIFT', 'AUTO', file, '-SS', 'SPATIAL', '0.004',
                                       '-DROP_GLOBAL_SHIFT', '-SAVE_CLOUDS', 'FILE', cc_saved], shell=True)


if __name__ == '__main__':
    directory = input('Input directory containing PTXs: ')
    cloud_compare = r'C:\Program Files\CloudCompare\CloudCompare.exe'
    cloud_compare_merge(directory, cloud_compare)
    cloud_compare_ss(directory, cloud_compare)
    cloud_compare_final_merge(directory, cloud_compare)
    cloud_compare_final_ss(directory, cloud_compare)
