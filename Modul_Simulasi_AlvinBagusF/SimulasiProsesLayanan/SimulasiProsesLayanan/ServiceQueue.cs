using System;
using System.Collections.Generic;

namespace SimulasiProsesLayanan
{
    public class ServiceQueue
    {
        private Queue<Customer> queue = new Queue<Customer>();

        public void AddCustomer(Customer customer)
        {
            queue.Enqueue(customer);
            Console.WriteLine($"{customer.Name} masuk dalam antrean.");
        }

        public void ProcessNext()
        {
            if (queue.Count > 0)
            {
                var next = queue.Dequeue();
                Console.WriteLine($"Melayani {next.Name}...");
            }
            else
            {
                Console.WriteLine("Antrean kosong.");
            }
        }

        public void ShowQueue()
        {
            Console.WriteLine("Antrean saat ini:");
            foreach (var c in queue)
            {
                Console.WriteLine($"- {c.Name}");
            }
        }
    }
}
